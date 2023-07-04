from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme', views.about_me, name='aboutme'),
    path('detail/<int:BlogPost_id>', views.detail, name='detail'),
    path('comment/reply/', views.reply_page, name="reply"),
]