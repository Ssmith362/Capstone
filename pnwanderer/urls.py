from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme', views.about_me, name='aboutme'),
    path('detail', views.detail, name='detail')
]