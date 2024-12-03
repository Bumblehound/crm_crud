from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name=""), # Keep the "name" the same as the route name
   path('register/', views.register, name="register"), 
]
