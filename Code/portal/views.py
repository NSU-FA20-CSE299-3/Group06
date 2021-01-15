# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from portal.models import Syllabus, Class_routine, Employment


def index(request):
    return render(request, 'portal/home.html')


def academic(request):
    return render(request, 'portal/home.html')


def class_routine(request):
    class_routines = Class_routine.objects.all()
    print(class_routines)
    params = {'class_routines': class_routines}
    return render(request, 'portal/class_routine.html', params)


def syllabus(request):
    syllabuses = Syllabus.objects.all()
    print(syllabuses)
    params = {'syllabuses': syllabuses}
    return render(request, 'portal/syllabus.html', params)


def admission(request):
    return HttpResponse("Welcome to admission activities")


def employment(request):
    employees = Employment.objects.all()
    print(employees)
    params = {'employees': employees}
    return render(request, 'portal/employee.html', params)


def gallery(request):
    return HttpResponse("Welcome to portal gallery")


def about(request):
    return render(request, 'portal/about.html')


def contact(request):
    return HttpResponse("Welcome to Contact Page ")
