from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from portal.models import Academic, Syllabus


def index(request):
    return render(request, 'portal/home.html')


def academic(request):
    academics = Academic.objects.all()
    print(academics)
    params = {'academic': academics}
    return render(request, 'portal/academic.html', params)


def syllabus(request):
    syllabuses= Syllabus.objects.all()
    print(syllabuses)
    params ={'syllabuses': syllabuses}
    return render(request,'portal/syllabus.html',params)


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
