from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from blogpy_articles.models import UserProfile
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.


def sidebar_render_partial(request, *args, **kwargs):
    user = User.objects.filter(id=request.user.id).first()
    profile = UserProfile.objects.filter(user=user).first()
    context = {
        "user_profile": profile,
    }
    return render(request, "sidebar.html", context)


@login_required(login_url="/accounts/login/")
def user_home(request):
    user = User.objects.filter(id=request.user.id).first()
    context = {
        "user": user
    }

    return render(request, "user_home.html", context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "login_form": login_form
    }
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            context["login_form"] = LoginForm()
            return redirect('/accounts')
        else:
            login_form.add_error('user_name', 'کاربری با این مشخصات وجود ندارد')
    return render(request, "login.html", context)


def log_out(request):
    logout(request)
    return redirect("/accounts/login/")
