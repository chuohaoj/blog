#blog/blogapp/urls.py

from django.conf.urls import url

from blogapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]

app_name = 'blog'