from django.contrib import admin
from .models import NavBarAndFooter, AccreditationAndMembership,TopImageOfAllPage
# Register your models here.
from .models import LegalContain
# Register your models here.

class LegalContainAdmin(admin.ModelAdmin):
    list_display = ('legal_title',)

admin.site.register(LegalContain, LegalContainAdmin)

admin.site.register(NavBarAndFooter)
admin.site.register(AccreditationAndMembership)
admin.site.register(TopImageOfAllPage)