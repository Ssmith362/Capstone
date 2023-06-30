from django.shortcuts import render, get_object_or_404
from . models import BlogPost

def home(request):

    blog_posts = BlogPost.objects.all().order_by('-id')
    context = {'blog_posts': blog_posts}
    return render(request, 'pnwanderer/home.html', context)

def about_me(request):
    return render(request, 'pnwanderer/aboutme.html')

def detail(request, BlogPost_id):
    detailed_post = get_object_or_404(BlogPost, pk=BlogPost_id)
    context = {'detailed_post': detailed_post}
    print('Detailed post', detailed_post.images.all())
    return render(request, 'pnwanderer/detail.html', context)