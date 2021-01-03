from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
def index (request):
     return render(request, 'portal/home.html')
def academic(request):
     return HttpResponse("Welcome to academic activities")
def admission(request):
     return HttpResponse("Welcome to admission activities")
def employment(request):
     return HttpResponse("Welcome to academic section")
def gallery(request):
     return HttpResponse("Welcome to portal gallery")
def about(request):

     return render(request, 'portal/about.html')
def contact(request):
     return HttpResponse("Welcome to Contact Page ")
