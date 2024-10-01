from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites_list, name='favourites-list'),  
    path('favourite/<int:post_id>/', views.favourite_post, name='favourite-post'),  
]