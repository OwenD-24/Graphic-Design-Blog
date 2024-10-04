from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='user-profile'),  
    path('profile/<str:username>/update/', views.profile_update, name='profile-update'),
    path('login/', views.user_login, name='login'), 
]


