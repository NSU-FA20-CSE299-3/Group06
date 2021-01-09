from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'App_Login/index.html')


def login_page(request):
    return render(request, 'App_Login/login.html')


def user_profile(request):
    return render(request, 'App_Login/profile.html')


def logout_user(request):
    return HttpResponse("Welcome to Portal")


def pass_change(request):
    return HttpResponse("change your password")
