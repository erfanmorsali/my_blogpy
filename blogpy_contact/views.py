from django.shortcuts import render
from .models import SiteInformation


# Create your views here.


def about_us(request):
    about = SiteInformation.objects.last()
    context = {
        "about": about
    }
    return render(request, "about_us.html", context)


def contact_us(request):
    about = SiteInformation.objects.last()
    context = {
        "about": about
    }
    return render(request, "contact_us.html", context)
