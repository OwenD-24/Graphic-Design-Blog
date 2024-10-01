from django.urls import path
from . import views

urlpatterns = [
    path('favourite/<int:post_id>/', views.favourite_post, name='favourite-post'),
]