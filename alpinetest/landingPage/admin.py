from django.contrib import admin

from .models import ISlidingImage, IIMobileView, IIIMigrationComplexSection
from .models import IVMigrationComplexImageSection, VAboutSection, VIAbout_Mission_Vision_Value_Section
from .models import  VIIAbout_Us_Question, VIIIAbout_Us_Answer,IXAfterAboutOurCompanySection,XService_Section
from .models import XIService_Add_Section, XIIResources_Background_Image_Section, XIIIResources_Description_Section

# Register your models here.

class ISlidingImageAdmin(admin.ModelAdmin):
    list_display=('description_1', )
admin.site.register(ISlidingImage, ISlidingImageAdmin)

class IIMobileViewAdmin(admin.ModelAdmin):
    list_display=('description_1', )
admin.site.register(IIMobileView, IIMobileViewAdmin)


class IIIMigrationComplexSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'heading',)
admin.site.register(IIIMigrationComplexSection, IIIMigrationComplexSectionAdmin)


class IVMigrationComplexImageSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'heading',)
admin.site.register(IVMigrationComplexImageSection, IVMigrationComplexImageSectionAdmin)


class VAboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(VAboutSection, VAboutSectionAdmin)

admin.site.register(VIAbout_Mission_Vision_Value_Section)

class VIIAbout_Us_QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)
admin.site.register(VIIAbout_Us_Question, VIIAbout_Us_QuestionAdmin)


class VIIIAbout_Us_AnswerAdmin(admin.ModelAdmin):
    list_display = ('question_category',)
admin.site.register(VIIIAbout_Us_Answer, VIIIAbout_Us_AnswerAdmin)


class IXAfterAboutOurCompanySectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(IXAfterAboutOurCompanySection, IXAfterAboutOurCompanySectionAdmin)


class XService_SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(XService_Section, XService_SectionAdmin)

class XIService_Add_SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(XIService_Add_Section, XIService_Add_SectionAdmin)


admin.site.register(XIIResources_Background_Image_Section)

class XIIIResources_Description_SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(XIIIResources_Description_Section, XIIIResources_Description_SectionAdmin)
