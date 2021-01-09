from django.urls import path
from. import views

urlpatterns = [
  path("",views.index, name="App Login"),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
]
