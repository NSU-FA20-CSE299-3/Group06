from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'App_Login/index.html')


def login_page(request):
    return HttpResponse('Please log in to Portal')

