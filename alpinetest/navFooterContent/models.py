from django.db import models

# Create your models here.


class NavBarAndFooter(models.Model):
    top_nav_image = models.ImageField(upload_to='photos/navFooter')
    mobile_view_top_image = models.ImageField(upload_to='photos/navFooter')
    top_left_button_name =  models.CharField(max_length=100, blank=True)
    top_left_button_hyperlink =  models.TextField(max_length=500,blank=True)
    top_right_button_name = models.CharField(max_length=100, blank=True)
    top_right_button_hyperlink = models.TextField(max_length=500,blank=True)
    footer_consultation_title = models.TextField(max_length=500,blank=True)
    footer_consultation_title_description = models.TextField(max_length=500,blank=True)
    footer_consultation_button_name= models.TextField(max_length=500,blank=True)
    footer_consultation_hyperlink= models.TextField(max_length=500,blank=True)
    footer_consultation_image = models.ImageField(upload_to='photos/navFooter')
    footer_accreditations_memberships_title = models.TextField(max_length=500,blank=True)
    footer_legal_title = models.TextField(max_length=500,blank=True)
    footer_australia_flag = models.ImageField(upload_to='photos/navFooter')
    footer_australia_headoffice_title = models.TextField(max_length=300,blank=True)
    footer_australia_address = models.TextField(max_length=300,blank=True)
    footer_australia_facebook_link = models.TextField(max_length=500,blank=True)
    footer_australia_instagram_link = models.TextField(max_length=500,blank=True)
    footer_nepali_flag = models.ImageField(upload_to='photos/navFooter')
    footer_nepal_headoffice_title=models.TextField(max_length=300,blank=True)
    footer_nepali_address = models.TextField(max_length=300,blank=True)
    footer_nepali_facebook_link = models.TextField(max_length=500,blank=True)
    footer_nepali_instagram_link = models.TextField(max_length=500,blank=True)

    def __str__(self):
        title = 'Nav-Bar'
        return title



class AccreditationAndMembership(models.Model):
    image = models.ImageField(upload_to='photos/accred')


class LegalContain(models.Model):
    legal_title =  models.TextField(max_length=500, blank=True)
    legal_title_hyperlink = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.legal_title


class TopImageOfAllPage(models.Model):
    image = models.ImageField(upload_to='photos/top')
    
    def __str__(self):
        return "Same for all page"