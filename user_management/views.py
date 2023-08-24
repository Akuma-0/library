from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from .models import ProfileEditForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'user_management/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/User/login")
    else:
        form = UserCreationForm()
    return render(request, 'user_management/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/User/login')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/User/profile')  # Redirect to the user's profile page
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'user_management/edit_profile.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'user_management/user_profile.html', {'user': request.user})
