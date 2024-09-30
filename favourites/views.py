from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Favourite

@login_required
def favourites_list(request):
    favourites = Favourite.objects.filter(user=request.user)
    context = {
        'favourites': favourites
    }
    return render(request, 'favourites/favourites_list.html', context)

