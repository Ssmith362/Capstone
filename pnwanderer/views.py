from django.shortcuts import render
from . models import BlogPost

def home(request):

    blog_posts = BlogPost.objects.all()
    context = {'blog_posts': blog_posts}
    return render(request, 'pnwanderer/home.html', context)

def about_me(request):
    return render(request, 'pnwanderer/aboutme.html')