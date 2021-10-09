from django.contrib import admin
from .models import AboutUs, CoreValue, CompanyQuality, TopAboutUsDetails
# Register your models here.


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['heading',]

admin.site.register(AboutUs, AboutUsAdmin)

class CoreValueAdmin(admin.ModelAdmin):
    list_display = ['title',]

admin.site.register(CoreValue, CoreValueAdmin)


class CompanyQualityAdmin(admin.ModelAdmin):
    list_display=['title',]

admin.site.register(CompanyQuality, CompanyQualityAdmin)

class TopAboutUsDetailsAdmin(admin.ModelAdmin):
    list_display=['description',]

admin.site.register(TopAboutUsDetails, TopAboutUsDetailsAdmin)
