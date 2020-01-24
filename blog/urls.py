from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<slug:name>/', PostView.as_view(), name='post'),
    path('category/<slug:name>/', CategoryView.as_view(), name='category'),
    path('comment/<slug:name>/', CommentView.as_view(), name='comment'),
    path('private/', PrivateView.as_view(), name='private'),
    path('contact/', ContactView.as_view(), name='contact')

]
