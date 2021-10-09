from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class TopAboutUsDetails(models.Model):
    image = models.ImageField(upload_to="photos/blog", blank=True, null=True)
    description = models.TextField(max_length=100,  default="About Us")

    def __str__(self):
        return self.description

class AboutUs(models.Model):
    title_1                 = models.CharField(max_length=50,blank=True)
    title_2                 = models.CharField(max_length=50,blank=True)
    description_1           = models.TextField(max_length=150,blank=True)
    description_2           = models.TextField(max_length=150,blank=True)
    heading                 = models.CharField(max_length=20,blank=True)
    heading_description     = RichTextField(blank=True)
    logo                    = models.ImageField(upload_to="photos/about", blank=True)
    background_image        = models.ImageField(upload_to="photos/about", blank=True)
    title                   = models.TextField(max_length=100,blank=True)
    card_side_image         = models.ImageField(upload_to="photos/about", blank=True)
    core_title              = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.heading


class CoreValue(models.Model):
    image               = models.ImageField(upload_to="photos/about", blank=True)
    title               = models.CharField(max_length=50,blank=True)
    description         = models.TextField(max_length=150,blank=True)

    def __str__(self):
        return self.title


class CompanyQuality(models.Model):
    title = models.CharField(max_length=50,blank=True)
    description = models.TextField(max_length=150, blank=True)
    font_awesome_class_name =  models.CharField(max_length=30,blank=True)

    class Meta:
        verbose_name='CompanyQuality'  # this variable name should be exactly same
        verbose_name_plural='CompanyQualities'

    def __str__(self):
        return self.title