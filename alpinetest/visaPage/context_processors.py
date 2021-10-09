from .models import VisaCategory, CopyName

def visa_category(request):
    visa_cats = VisaCategory.objects.all()
    company_name = CopyName.objects.all().first()

    return dict(visa_cats=visa_cats, company_name=company_name)
