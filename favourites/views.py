from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .models import Favourite


@login_required
def favourites_list(request):
    favourites = Favourite.objects.filter(user=request.user)
    favourite_post_ids = favourites.values_list("post_id", flat=True)
    context = {
        "favourites": favourites,
        "favourite_post_ids": favourite_post_ids,
    }
    return render(request, "favourites/favourites_list.html", context)


@login_required
def favourite_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    favourite, created = Favourite.objects.get_or_create(user=request.user, post=post)
    if not created:
        favourite.delete()

    return redirect("post-detail", pk=post_id)
