from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
  path("",views.index, name="App Login"),
  path("academic/",views.academic,name="Academic"),
  path("academic/syllabus",views.syllabus,name="Syllabus"),
  path("admission/",views.admission,name="Admission"),
  path("employment/",views.employment,name="Employment"),
  path("gallery/",views.gallery,name="Gallery"),
  path("about/",views.about,name="About Us"),
  path("contact/",views.contact,name="Contact"),


]
