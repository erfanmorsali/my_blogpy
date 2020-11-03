from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Article,UserProfile


def home_page(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "home_page.html", context)


