from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name=""), # Keep the "name" the same as the route name

   path('login/', views.login, name="login"),
   path('logout/', views.logout, name="logout"),
   path('register/', views.register, name="register"), 

   # CRUD URLs
   path('dashboard/', views.dashboard, name="dashboard"),    
   path('create-record/', views.create_record, name="create-record"),   
   path('record/<int:pk>/', views.view_record, name="record"),  
   path('update-record/<int:pk>/', views.update_record, name="update-record"),    
   path('delete-record/<int:pk>/', views.delete_record, name="delete-record"),    
      

]
