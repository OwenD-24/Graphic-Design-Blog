from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='user-profile'),  
    path('profile/update/', views.profile_update, name='profile-update'),  
]
