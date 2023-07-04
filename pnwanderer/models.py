from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/', blank=True, null=True)
    summary = models.TextField(max_length=2000)
    full_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse("detail", kwargs={"BlogPost_id": self.pk})
    

    def get_comments(self):
        return self.comments.all()
    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(BlogPost, default=None, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to = 'blog_galleries/%Y/%m/%d/')
    def __str__(self):
        return self.post.title
       
class Comment(models.Model):
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(max_length=50)
    parent=models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)
