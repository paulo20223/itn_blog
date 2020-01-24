from django.forms import ModelForm
from blog.models import Comment, Info


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'email', 'message']
