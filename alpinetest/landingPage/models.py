from django.db import models

# Create your models here.

class ISlidingImage(models.Model):
    image = models.ImageField(upload_to="photos/home")
    description_1 = models.TextField(max_length=200, blank=True)
    description_2 = models.TextField(max_length=200, blank=True)
    description_3 = models.TextField(max_length=200, blank=True)
    button_name = models.CharField(max_length=100, blank=True)
    button_hyperlink=models.TextField(max_length=500, blank=True)
    qr_code = models.ImageField(upload_to="photos/home", blank=True, null=True)
    is_qr = models.BooleanField(default=True)

    def __str__(self):
        return self.description_1

class IIMobileView(models.Model):
    image = models.ImageField(upload_to="photos/home")
    description_1 = models.TextField(max_length=200, blank=True)
    description_2 = models.TextField(max_length=200, blank=True)
    occupation_button_name = models.CharField(max_length=100, blank=True)
    occupation_button_hyperlink=models.TextField(max_length=500, blank=True)
    contact_button_name = models.CharField(max_length=100, blank=True)
    contact_button_hyperlink = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description_1


class IIIMigrationComplexSection(models.Model):
    title = models.CharField(max_length=200, blank=True)
    heading = models.CharField(max_length=200, blank=True)
    sub_heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class IVMigrationComplexImageSection(models.Model):
    image = models.ImageField(upload_to="photos/home")
    title = models.CharField(max_length=200, blank=True)
    heading = models.TextField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    hyperlink = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title



class VAboutSection(models.Model):
    logo = models.ImageField(upload_to="photos/home")
    title = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title

class VIAbout_Mission_Vision_Value_Section(models.Model):
    mission= models.TextField(max_length=500,blank=True)
    vision= models.TextField(max_length=500,blank=True)
    value= models.TextField(max_length=500,blank=True)


class VIIAbout_Us_Question(models.Model):
    question = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.question

class VIIIAbout_Us_Answer(models.Model):
    answer = models.TextField(blank=True)
    question_category = models.ForeignKey(VIIAbout_Us_Question, on_delete=models.CASCADE)
    want_print_question = models.BooleanField(default=False)

    def __str__(self):
        return self.question_category.question


class IXAfterAboutOurCompanySection(models.Model):
    background_image = models.ImageField(upload_to="photos/home")
    title = models.CharField(max_length=200, blank =True)
    button_name = models.CharField(max_length=100, blank=True)
    button_hyperlink = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    


class XService_Section(models.Model):
    title = models.TextField(max_length=300, blank =True)
    heading = models.TextField(max_length=300, blank =True)
    description=models.TextField(blank =True)
    description_click = models.TextField(max_length=300, blank=True)
    email= models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

class XIService_Add_Section(models.Model):
    image = models.ImageField(upload_to="photos/home")
    title = models.TextField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    hyperlink=models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class XIIResources_Background_Image_Section(models.Model):
    image = models.ImageField(upload_to="photos/home")

class XIIIResources_Description_Section(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=300, blank=True)
    font_awesome_class_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
