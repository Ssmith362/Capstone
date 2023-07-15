from django.shortcuts import render, get_object_or_404, redirect
from . models import BlogPost, Comment
from .forms import CommentForm
import requests, math



def home(request):

    blog_posts = BlogPost.objects.all().order_by('-id')
    context = {'blog_posts': blog_posts}
    return render(request, 'pnwanderer/home.html', context)

def about_me(request):
    return render(request, 'pnwanderer/aboutme.html')

def detail(request, BlogPost_id):
    detailed_post = get_object_or_404(BlogPost, pk=BlogPost_id)
    

    location = detailed_post.lat + ',' + detailed_post.long

    get_weather = f"http://api.weatherstack.com/forecast?access_key=a84722bc00de8a28621386d7a4f6bbad&query={location}&current"
    weather = requests.get(get_weather).json()
    current_temperature = weather['current']['temperature']
    temperature_fehrenheit = (1.8 * current_temperature) + 32

    weather_icon = weather['current']['weather_icons']
    weather_description = weather['current']['weather_descriptions'][0]


    


    fav = bool
    if detailed_post.favorites.filter(id=request.user.id).exists():
        fav=True
            
    # List of active comments for this post
    comments = detailed_post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            post = BlogPost.objects.get(id=BlogPost_id)
            new_comment.post = post

            # Save the comment to the database
            new_comment.save()
            # redirect to same page and focus on that comment
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
        else:
            comment_form = CommentForm()
    
    return render(request, 'pnwanderer/detail.html', {'detailed_post': detailed_post,'comments': comments,'comment_form':comment_form, 'fav':fav, 'weather': weather, 'temperature_fehrenheit':temperature_fehrenheit, 'weather_description': weather_description})


def reply_page(request):
    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():
            post_id = request.POST.get('post_id')  
            parent_id = request.POST.get('parent')  
            post_url = request.POST.get('post_url') 
            reply = form.save(commit=False)
            post = BlogPost.objects.get(id=post_id)
            reply.post = BlogPost.objects.get(id=post_id)
            reply.parent = Comment.objects.get(id=parent_id)
            reply.save()

            return redirect(post.get_absolute_url()+'#'+str(reply.id))

    return redirect("/")






