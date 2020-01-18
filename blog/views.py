from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, View

from blog.forms import CommentForm
from blog.models import Post, Comment, Video


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date_creation')
        context['videos'] = Video.objects.all().order_by('-date_creation')

        context['general'] = context['posts'].first()
        context['header_posts'] = Post.objects.filter(is_header=True)
        return context


class PostView(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, url_name=kwargs.get("name"))
        context['comments'] = Comment.objects.filter(post=context['post']).order_by('-date_creation')
        return context


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category__name=kwargs.get('category')).order_by('-date_creation')
        context['header_posts'] = Post.objects.filter(is_header=True)
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


class PrivateView(TemplateView):
    template_name = 'private.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
