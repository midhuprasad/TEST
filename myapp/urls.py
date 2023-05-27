from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login,name='Login'),
    path('register/', views.register,name='register'),
    path('Home/', views.Home,name='Home'),
   
]