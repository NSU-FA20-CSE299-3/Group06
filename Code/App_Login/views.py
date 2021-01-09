from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'App_Login/index.html')


def login(request):
    return HttpResponse("Welcome to Portal")


def logout(request):
    return HttpResponse("Welcome to Portal")
