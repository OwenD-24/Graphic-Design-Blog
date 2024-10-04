from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            Profile.objects.create(user=user)  
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}. You can log in now!')
            return redirect('login')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'user': user})

@login_required
def profile_update(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)

        if u_form.is_valid() and p_form.is_valid():
            try:
                u_form.save()
                p_form.save()
                messages.success(request, 'Your account has been updated!')
                return redirect('user-profile', username=user.username)
            except Exception as e:
                messages.error(request, f'Error saving profile: {str(e)}')
        else:
            messages.error(request, 'There were errors in the form.')
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, 'users/profile_update.html', context)

from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.user.is_authenticated:  
        return redirect('blog-home')  

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('blog-home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})




