from django.shortcuts import render, redirect
from .models import Article


def home_page(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "home_page.html", context)


