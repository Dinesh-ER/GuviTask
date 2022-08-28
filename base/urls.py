from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/check/', views.register_check, name='register_check'),
    path('login/', views.login, name='login'),
    path('login/check/', views.login_check, name='login_check'),
    path('user/<username>/', views.profile, name='profile'),
    path('user/<username>/edit/', views.edit_profile, name='edit_profile'),
    path('user/<username>/save/', views.save_profile, name='save_profile'),
    
    

]











