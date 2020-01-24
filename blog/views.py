from itertools import groupby

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.defaulttags import GroupedResult
from django.views.generic import TemplateView

from blog.forms import CommentForm, InfoForm
from blog.models import Post, Comment, Video, Settings, Category
from blog.telegram import Bot


class AbsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(is_show=True).order_by('-date_creation')
        context['header_posts'] = Post.objects.filter(is_header=True)

        context['settings'] = {}
        for setting in Settings.objects.all():
            context['settings'][setting.name] = setting.value

        return context

    @staticmethod
    def __insert_paginator(iterable_object, page, items_for_one_page):
        paginator = Paginator(iterable_object, items_for_one_page)
        try:
            iterable_object_selection = paginator.page(page)
        except PageNotAnInteger:
            iterable_object_selection = paginator.page(1)
        except EmptyPage:
            iterable_object_selection = paginator.page(paginator.num_pages)
        return iterable_object_selection

    def get_paginator(self, iterable_object, items_for_one_page=10):
        page = self.request.GET.get('page')
        return self.__insert_paginator(iterable_object, page, items_for_one_page)


class HomeView(AbsView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_by_category'] = {}
        context['general'] = Post.objects.first()
        context['header_posts'] = Post.objects.filter(is_header=True)

        for post in Post.objects.select_related('category').all().order_by('-date_creation'):
            context["posts_by_category"].setdefault(post.category, [])
            if len(context["posts_by_category"][post.category]) < 5:
                context["posts_by_category"][post.category].append(post)
        return context


class PostView(AbsView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, url_name=kwargs.get("name"))
        context['comments'] = Comment.objects.filter(post=context['post']).order_by('-date_creation')
        return context


class CategoryView(AbsView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_paginator(
            Post.objects.filter(category__name=kwargs.get('name')).order_by('-date_creation'))

        return context


class CommentView(TemplateView):
    template_name = 'post.html'

    def post(self, request, **kwargs):
        post = get_object_or_404(Post, url_name=kwargs.get("name"))

        form = CommentForm(request.POST or None)
        if form.is_valid():
            model = form.save()
            form.instance.user = self.request.user
            form.instance.post = post
            model.save()
        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])


class PrivateView(AbsView):
    template_name = 'private.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactView(AbsView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, **kwargs):
        form = InfoForm(request.POST)
        if form.is_valid():
            message = "\n".join(['%s: %s' % (key, value) for (key, value) in form.cleaned_data.items()])
            print(Bot().send_message(message))
            messages.success(request, 'Success!')
            form.save()
        else:
            messages.success(request, 'Not valid!')

        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])
