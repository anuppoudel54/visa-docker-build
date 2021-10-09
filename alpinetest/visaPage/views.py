from django.shortcuts import render, get_object_or_404

from .models import VisaCategory, TypeOfSubVisa, SubVisa, VisaPageDescription, VisaDetailsDescription, UseFullQuestion, VisaTopSection



def visa(request):
    visa_top = VisaTopSection.objects.all().first()
    visa_cats = VisaCategory.objects.all()
    descriptions = VisaPageDescription.objects.all()
    context={
        'visa_cats':visa_cats,
        'descriptions':descriptions,
        'visa_top':visa_top,
    }
    return render(request, 'visa.html', context)


def subvisa(request, visa_slug):
    visas = get_object_or_404(VisaCategory, slug=visa_slug)
    sub_visas = SubVisa.objects.all().filter(visa__slug = visa_slug)
    single_visas = TypeOfSubVisa.objects.all().filter(visa = visas)
    visa_description = VisaDetailsDescription.objects.get(visa__slug = visa_slug)

    existed = UseFullQuestion.objects.all().filter(visa=visas).exists()
    usefull=None
    if existed:
        usefull = UseFullQuestion.objects.all().filter(visa=visas)
    context={
        'single_visas':single_visas,
        'visa_description':visa_description,
        'usefull':usefull,
        'existed':existed,
        'visas':visas,
    }  

    return render(request, 'visa_details.html', context)