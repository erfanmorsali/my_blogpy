from django.contrib import admin
from .models import SiteInformation
# Register your models here.

class SiteInformationAdmin(admin.ModelAdmin):
    list_display = ["__str__" , "email" , "phone"]


admin.site.register(SiteInformation)