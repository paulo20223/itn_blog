import re
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.contrib.postgres.forms import JSONField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    url_name = models.CharField(max_length=1000, verbose_name='URL страницы', unique=True)
    title = models.CharField(max_length=1000, verbose_name='Название поста', unique=True, default="")
    title_description = models.CharField(max_length=1000, verbose_name='Краткое описание поста', null=True, blank=True)
    image = models.ImageField('Фото поста', null=True, blank=True)
    text = RichTextUploadingField(verbose_name="Текст поста")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    hidden_post = models.BooleanField(default=False, verbose_name='Скрыть пост с главной')
    is_header = models.BooleanField(default=False, verbose_name='Отображать в заголовке')
    count_block_in_line = models.IntegerField(default=3, verbose_name="Размер блока",
                                              help_text='Размер поста на главной странице (от 1 до 12')
    date_creation = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время последнего изменения', auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title} ({self.category})'

    def col(self):
        return int(12 / self.count_block_in_line)


class Video(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    url = models.CharField(max_length=1000, verbose_name='Ссылка')
    is_show = models.BooleanField(default=True, verbose_name="Отображать в сайдбаре")
    date_creation = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время последнего изменения', auto_now=True)

    def filter_url(self):
        return next(iter(re.findall(r'=(\w{10,15})', self.url)))

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f'{self.title} ({self.url})'


class Comment(models.Model):
    message = models.TextField(verbose_name="Сообщение")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    date_creation = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время последнего изменения', auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.message} ({self.user}). Пост: {self.post}'


class Info(models.Model):
    email = models.EmailField(verbose_name="Еmail")
    name = models.CharField(max_length=1000, verbose_name='Имя')
    message = models.TextField(verbose_name="Сообщение")
    date_creation = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время последнего изменения', auto_now=True)
    dop_info = JSONField()

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return f'{self.email} ({self.name}'


settings = (('telegram_link', "Телеграмм ссылка"),
            ('ref_link', 'Реферальная ссылка'),
            ('youtube_link', 'Youtube ссылка'),
            ('patreon_link', 'Patreon ссылка'),
            ('bot_token', "Telegram. Bot token"),
            ('bot_chats_id', 'Telegram. id чата'))


class Settings(models.Model):
    name = models.CharField(max_length=1000, choices=settings, verbose_name="Название настройки", unique=True)
    value = models.CharField(max_length=1000, verbose_name="Название настройки")

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
