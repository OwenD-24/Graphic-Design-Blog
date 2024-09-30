from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Favorite

@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {
        'favorites': favorites
    }
    return render(request, 'favorites/favorites_list.html', context)

