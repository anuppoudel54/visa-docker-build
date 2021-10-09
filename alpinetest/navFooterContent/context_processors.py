from .models import NavBarAndFooter
from .models import AccreditationAndMembership

from .models import LegalContain, TopImageOfAllPage


def nav_footor_content(request):
    navFooters = NavBarAndFooter.objects.all()
    navFooter = None
    for nav in navFooters:
        navFooter = nav
        break
    images = AccreditationAndMembership.objects.all()
    legalcontains = LegalContain.objects.all()
    
    
    from datetime import date
    today = date.today()
    topImage = TopImageOfAllPage.objects.all().first()

    return dict(navFooter=navFooter, images=images, legalcontains=legalcontains, year = today.year,topImage=topImage)