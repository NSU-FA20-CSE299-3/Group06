from django.urls import path
from. import views

urlpatterns = [
  path("",views.index, name="App Login"),
  path('login/', views.login_page, name='login'),
  path('profile/', views.user_profile, name='profile'),
  path('logout/', views.logout_user, name='logout'),
  path('password/', views.pass_change, name='pass_change'),
]
