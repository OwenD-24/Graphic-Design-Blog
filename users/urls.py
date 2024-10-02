from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='users-profile'),
    path('profile/update/', views.profile_update, name='profile-update'), 
]
