from django.urls import path, include
from . import views
from .views import (PostCreateView, PostDeleteView, PostDetailView,
                    PostListView, PostUpdateView)

urlpatterns = [
    path('about/', views.about, name="blog-about"),
    path('', PostListView.as_view(), name="blog-home"), 
    path('post-new/', PostCreateView.as_view(), name="blog-post-form"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="blog-update"), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),
]

