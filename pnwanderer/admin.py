from django.contrib import admin
from .models import BlogPost, PostImage, Comment


admin.site.register(BlogPost)

admin.site.register(PostImage)

admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')