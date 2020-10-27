from django.shortcuts import render,redirect


def home_page(request):
    return render(request,"home_page.html",{})

def about_us(request):
    return render(request,"about_us.html",{})