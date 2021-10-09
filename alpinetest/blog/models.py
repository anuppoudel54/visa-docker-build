from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from embed_video.fields import EmbedVideoField

# Create your models here.

class BlogTopSection(models.Model):
    image  = models.ImageField(upload_to="photos/blog", blank=True,null=True)
    title = models.TextField(max_length=100,  blank=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    blog_top_image = models.ImageField(upload_to="photos/blog", blank=True, null=True)
    blog_top_description = models.TextField(max_length=100,  default="BLOG SINGLE")
    image = models.ImageField(upload_to="photos/blog", blank=True, null=True)
    title = models.TextField(max_length=100,  unique=True)
    slug = models.TextField(max_length=100,  unique=True)
    short_description = models.TextField(max_length=100)
    description = RichTextField(blank=True)
    youtube_video=EmbedVideoField(max_length=500, blank=True, null=True)
    quote_image = models.ImageField(upload_to="photos/blog", blank=True, null=True)
    quote_of_the_day = models.TextField(max_length=200,  blank=True)
    author = models.CharField(max_length=100, blank=True)
    created_date      = models.DateField(auto_now_add=True)
    modified_date     = models.DateField(auto_now=True)


    def get_url(self):
        return reverse("blog_content", args=[self.slug])


    def __str__(self):
        return self.title




class BlogComment(models.Model):
    blog        = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    phone       = models.CharField(max_length=15)
    email       = models.EmailField()
    comment     = models.TextField(max_length=500)
    created_date      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name