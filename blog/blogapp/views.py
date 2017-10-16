#blog/blogapp/views.py


from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'blogapp/index.html', context = {
                    'title': 'My first page',
                    'Welcome': 'welcome to my blog'
                    })