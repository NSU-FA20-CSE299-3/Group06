from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'App_Login/index.html')


def login_page(request):
    return HttpResponse('Please log in to Portal')


def logout_user(request):
    return HttpResponse("Welcome to Portal")


def pass_change(request):
    return HttpResponse("change your password")
