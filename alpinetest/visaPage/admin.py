from django.contrib import admin
from .models import VisaCategory, SubVisa, TypeOfSubVisa, VisaPageDescription, VisaDetailsDescription, UseFullQuestion, VisaTopSection, CopyName

# Register your models here.
admin.site.register(CopyName)
admin.site.register(VisaTopSection)

class VisaCategoryAdmin(admin.ModelAdmin):
    list_display = ('visa_title',)
    prepopulated_fields ={'slug': ('visa_title',)}


admin.site.register(VisaCategory, VisaCategoryAdmin)


class SubVisaAdmin(admin.ModelAdmin):
    list_display =('sub_visa_title', 'visa')

admin.site.register(SubVisa, SubVisaAdmin)

class TypeOfSubVisaAdmin(admin.ModelAdmin):
    list_display =('visa', 'sub_visa_title', 'type_sub_visa_title' ,'are_you_including_name_of_sub_visa_first_time')

admin.site.register(TypeOfSubVisa,TypeOfSubVisaAdmin)


class VisaPageDescriptionAdmin(admin.ModelAdmin):
    list_display = ('description',)

admin.site.register(VisaPageDescription,VisaPageDescriptionAdmin)

class VisaDetailsDescriptionAdmin(admin.ModelAdmin):
    list_display=('visa','top_image_description')

admin.site.register(VisaDetailsDescription, VisaDetailsDescriptionAdmin)

class UseFullQuestionAdmin(admin.ModelAdmin):
    list_display=('visa','subvisa', 'question')

admin.site.register(UseFullQuestion, UseFullQuestionAdmin)