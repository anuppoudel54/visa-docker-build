
from django.urls import path
from . import views



urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-details/<slug:blog_slug>', views.blog_content, name="blog_content"),
    path('search/', views.search, name='search'),
    
]

