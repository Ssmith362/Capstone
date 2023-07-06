from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from pnwanderer.models import BlogPost
from django.http import HttpResponseRedirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='/users/login/')
def profile_view(request):
    new=request.user.favorite.all()
    
    return render(request, 'users/profile.html',{'new':new})

@login_required
def favorite_add(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if post.favorites.filter(id=request.user.id).exists():
        post.favorites.remove(request.user)
    else:
        post.favorites.add(request.user)
    return render(request, 'pnwanderer/detail.html', {'detailed_post': post})

@login_required
def favorite_list(request):
    # new=BlogPost.objects.filter(favorites=request.user)
    new=request.user.favorite.all()
    return render(request, 'profile.html', {'new': new})
