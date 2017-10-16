from django.shortcuts import render, get_object_or_404
from blogapp.models import Post
# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('modified_time')
    return render(request, 'blogapp/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blogapp/detail.html', context={'Post': post})