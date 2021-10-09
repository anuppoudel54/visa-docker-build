from django.db import models
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class VisaTopSection(models.Model):
    image  = models.ImageField(upload_to="photos/visa", blank=True,null=True)
    title = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.title

class VisaCategory(models.Model):
    # visa_page_description = models.TextField(blank=True)
    # are_you_including_description_first_time = models.BooleanField(default=False)
    visa_image = models.ImageField(upload_to="photos/visas", blank=True)
    visa_title = models.CharField(max_length=150, blank =True)
    slug = models.SlugField(max_length=200, unique=True)
    hover_description = models.TextField(max_length=250, blank=True)

    def get_url(self):
        return reverse('subvisa', args=[self.slug])

    def __str__(self):
        return self.visa_title

class SubVisa(models.Model):
    # sub_visa_top_description = models.TextField(blank=True)
    # sub_visa_image = models.ImageField(upload_to="photos/visas", blank=True)

    # are_you_including_description_first_time = models.BooleanField(default=False)
    visa = models.ForeignKey(VisaCategory, on_delete=models.CASCADE)
    sub_visa_title = models.TextField(max_length=300,blank=True)
    subvisa_body = RichTextField(blank=True)
    
    # type_of_subtype = models.ForeignKey(VisaCategory)
    def __str__(self):
        return self.sub_visa_title

class TypeOfSubVisa(models.Model):
    sub_visa_title = models.ForeignKey(SubVisa, on_delete=models.CASCADE)
    visa = models.ForeignKey(VisaCategory, on_delete=models.CASCADE)
    are_you_including_name_of_sub_visa_first_time = models.BooleanField(default=False)
    type_sub_visa_title = models.TextField(max_length=250, blank=True)
    type_of_subvisa_body = RichTextField(blank=True)
    font_awesome_class_name1 = models.TextField(max_length=100, blank=True, default='fas fa-dollar-sign')
    first_field1 = models.CharField(max_length=100, blank=True)
    second_field1 = models.CharField(max_length=200, blank=True)
    third_field1 = RichTextField(blank=True)
    font_awesome_class_name2 = models.TextField(max_length=100, blank=True, default='fas fa-hourglass-start')
    first_field2 = models.CharField(max_length=100, blank=True)
    second_field2 = models.CharField(max_length=200, blank=True)
    third_field2 = RichTextField(blank=True)
    font_awesome_class_name3 = models.TextField(max_length=100, blank=True, default='fas fa-plane-departure')
    first_field3 = models.CharField(max_length=100, blank=True)
    second_field3 = models.CharField(max_length=200, blank=True)
    third_field3 = RichTextField(blank=True)

    def __str__(self):
        return self.type_sub_visa_title


class VisaPageDescription(models.Model):
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.description

class VisaDetailsDescription(models.Model):
    visa = models.ForeignKey(VisaCategory, on_delete=models.CASCADE)
    top_image = models.ImageField(upload_to="photos/visas", blank=True)
    top_image_description =models.TextField(max_length=100, blank=True)
    description = RichTextField(blank=True)
    image = models.ImageField(upload_to="photos/visas", blank=True)

    def __str__(self):
        return self.description


class UseFullQuestion(models.Model):
    visa =models.ForeignKey(VisaCategory, on_delete=models.CASCADE)
    subvisa = models.ForeignKey(SubVisa, on_delete=models.CASCADE)
    heading = models.TextField(max_length=50, blank=True)
    question = models.TextField(max_length=500)
    answer = RichTextField()
    questionId = models.TextField(max_length=100)


    def __str__(self):
        return self.question
    
class CopyName(models.Model):
    name = models.TextField(max_length=100, blank=True, default="VISA ALLIANCE")
    address = models.TextField(max_length=50, blank=True, default="AUSTRALIA")

    def __str__(self):
        return self.name