from django.contrib import admin
from blog.models import *
from random import randint


def duplicate_post(model_admin, request, queryset):
    for obj in queryset:
        identify = randint(0, 10000000)
        obj.id = None
        obj.url_name = f"{obj.url_name}-{identify}"
        obj.title = f"{obj.title}-{identify}"

        obj.save()
    return None


duplicate_post.short_description = "Duplicate selected record"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [duplicate_post, ]


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    pass


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    fields = ('name', 'value')
    list_display = ('name', 'value')


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass
