from django.urls import path
from . import views
from blog.views import PostDetailView

urlpatterns = [
    path('', views.favourites_list, name='favourites-list'),  
    path('favourite/<int:post_id>/', views.favourite_post, name='favourite-post'),  
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  
]