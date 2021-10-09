from django.shortcuts import render

from landingPage.models import ISlidingImage, IIMobileView, IIIMigrationComplexSection
from landingPage.models import IVMigrationComplexImageSection, VAboutSection, VIAbout_Mission_Vision_Value_Section
from landingPage.models import  VIIAbout_Us_Question, VIIIAbout_Us_Answer,IXAfterAboutOurCompanySection,XService_Section
from landingPage.models import XIService_Add_Section, XIIResources_Background_Image_Section, XIIIResources_Description_Section
#from store.models import Product
def home(request):
    slide_images = ISlidingImage.objects.all()
    mobile=IIMobileView.objects.all()
    mobiles=None
    for mob in mobile:
        mobiles = mob
        break

        
    
    migrations = IIIMigrationComplexSection.objects.all()
    migrationimages = IVMigrationComplexImageSection.objects.all()
    abouts = VAboutSection.objects.all()
    missions =VIAbout_Mission_Vision_Value_Section.objects.all()
    about_questions = VIIAbout_Us_Question.objects.all()
    about_answers = VIIIAbout_Us_Answer.objects.all()
    follow_dreams = IXAfterAboutOurCompanySection.objects.all()
    services = XService_Section.objects.all()
    service_adds = XIService_Add_Section.objects.all()
    resource_image= XIIResources_Background_Image_Section.objects.all()
    resource_images=None
    for res in resource_image:
        resource_images = res
        break
    resource_descriptions = XIIIResources_Description_Section.objects.all()

    context = {
        'slide_images': slide_images,
        'mobiles':mobiles,
        'migrations':migrations,
        'migrationimages':migrationimages,
        'abouts':abouts,
        'missions':missions,
        'about_questions':about_questions,
        'about_answers':about_answers,
        'follow_dreams':follow_dreams,
        'services':services,
        'service_adds':service_adds,
        'resource_images':resource_images,
        'resource_descriptions':resource_descriptions
    }

    return render(request, 'home.html', context)