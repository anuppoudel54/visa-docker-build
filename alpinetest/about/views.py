from django.shortcuts import render
from .models import AboutUs, CoreValue, CompanyQuality, TopAboutUsDetails
# Create your views here.


def about(request):
    tops =TopAboutUsDetails.objects.all()
    about_us = AboutUs.objects.all()
    core_values = CoreValue.objects.all()
    qualities = CompanyQuality.objects.all()

    context ={
        'about_us':about_us,
        'core_values':core_values,
        'qualities':qualities,
        'tops':tops,
    }

    return render(request, 'about.html', context)
