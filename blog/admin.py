from django.contrib import admin
from blog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    pass
