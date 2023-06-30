from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/', blank=True, null=True)
    summary = models.TextField(max_length=2000)
    full_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(BlogPost, default=None, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to = 'blog_galleries/%Y/%m/%d/')
    def __str__(self):
        return self.post.title
