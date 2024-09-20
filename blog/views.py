from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return HttpResponse("<h1>Blog Home</h1>")

def about(request):
    return HttpResponse("<h1>Blog About</h1>")
