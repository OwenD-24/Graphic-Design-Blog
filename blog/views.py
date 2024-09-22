from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})

def post_detail(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'blog/post_detail.html', {'post': post})
