from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
import pymongo
from decouple import config
from .models import Users

client = pymongo.MongoClient(config("HOST"))
db = client['GuviTaskDB']['users']

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':        
        content = {
            'username': request.POST['username'],
            'email': request.POST['email'],
            'password': make_password(request.POST['password'])
        }
        db.insert_one(content)
        return redirect('login')  
    
    return render(request, 'register.html')
