from django.urls import path
from. import views

urlpatterns = [
  path("",views.index, name="App Login"),
  path('login/', views.login_page, name='login'),
  
]
