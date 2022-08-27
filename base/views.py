from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
import pymongo
from decouple import config
from .models import Users

client = pymongo.MongoClient(config("HOST"))
db = client['GuviTaskDB']['users']

def home(request):
    if request.session.get("auth"):
        return redirect('profile', username=request.session.get("username"))
        
    return render(request, 'home.html')


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

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        stored_password = Users.objects.get(username=username).password
        
        if check_password(password, stored_password):
            request.session['auth'] = True
            request.session['username'] = username
            return redirect('profile', username=username)
        
    return render(request, 'login.html')


def profile(request, username):
    if not request.session.get("auth"):
        return redirect('home')
    
    data = Users.objects.get(username=username)
    
    context = {
        "userData": {
            "username": data.username,
            "email": data.email,
            "contact": data.contact,
            "dob": data.dob,
            "age": data.age,
            "country": data.country
        }
    }
    
    return render(request, 'profile.html', context)

def edit_profile(request, username):
    data = Users.objects.get(username=username)
    
    context = {
        "userData": {
            "username": data.username,
            "email": data.email,
            "contact": data.contact,
            "dob": data.dob,
            "age": data.age,
            "country": data.country
        }
    }
    return render(request, 'edit.html', context)

def save_profile(request, username):
    
    if request.method == 'POST':
        content = {
            'username': request.POST['username'],
            "email": request.POST['email'],
            "contact": request.POST['contact'],
            "dob": request.POST['dob'],
            "country": request.POST['country']
        }
        db.update_one({"username": username}, {"$set": content})
        
        return redirect('profile', username=username)

        
