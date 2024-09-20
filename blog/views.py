from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

posts = [
    {
        'author': 'Owen Davis',
        'title': 'Blog Post 1',
        'content': 'This is my first blog post',
        'date_posted': '8th February, 2024',
    },
    {
        'author': 'Owen D',
        'title': 'Blog Post 2',
        'content': 'This is my second blog post',
        'date_posted': '13th February, 2024',
    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})
