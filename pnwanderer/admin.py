from django.contrib import admin
from .models import BlogPost, PostImage


admin.site.register(BlogPost)

admin.site.register(PostImage)