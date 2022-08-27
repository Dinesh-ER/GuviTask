from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user/<username>/', views.profile, name='profile'),
    path('user/<username>/edit/', views.edit_profile, name='edit_profile'),
    path('user/<username>/save/', views.save_profile, name='save_profile')
    
    

]











