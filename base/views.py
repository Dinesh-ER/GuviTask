from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
import pymongo
import codecs
import base64
from decouple import config
from dateutil.parser import parse
from .models import Users
from .utils import calculate_age

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
			'password': make_password(request.POST['password']),
			'contact': '',
			'dob': '',
			'age': None,
			'country': '',
			'is_verified': False
		}
		db.insert_one(content)
		return redirect('login')  
	
	return render(request, 'register.html')

def register_check(request):
	if request.method == "POST":
		username = request.POST['username']
		
		user_exist = Users.objects.filter(username=username).count() 
		print(user_exist)
		return JsonResponse({"status": bool(user_exist)})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		return redirect('profile', username=username)
		
	return render(request, 'login.html')

def login_check(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		msg = ''
		error = ''
		
		user_exist = Users.objects.filter(username=username).count()
  
		if user_exist:
			stored_password = Users.objects.get(username=username).password
			if check_password(password, stored_password):
				request.session['auth'] = True
				request.session['username'] = username
			else:
				error = "password"
				msg = "Incorrect Password."
		else:
			error = "user"
			msg = "User does not exist."   
		return JsonResponse({"error": error, "msg": msg})


def profile(request, username):
	if not request.session.get("auth"):
		return redirect('home')
	
	data = Users.objects.get(username=username)
	base64_data = codecs.encode(data.photo, 'base64')
	photo = base64_data.decode('utf-8') 
	
	context = {
		"userData": {
			"username": data.username,
			"email": data.email,
			"contact": data.contact,
			"dob": data.dob,
			"age": data.age,
			"country": data.country,
		},
		"photo": photo
	}
	return render(request, 'profile.html', context)

def edit_profile(request, username):
	data = Users.objects.get(username=username)
	base64_data = codecs.encode(data.photo, 'base64')
	photo = base64_data.decode('utf-8') 
	
	context = {
		"userData": {
			"username": data.username,
			"email": data.email,
			"contact": data.contact,
			"dob": data.dob,
			"age": data.age,
			"country": data.country
		},
		"photo": photo
	}
	return render(request, 'edit.html', context)

def save_profile(request, username):
	
	if request.method == 'POST':
		content = {
			"email": request.POST['email'],
			"contact": request.POST['contact'],
			"dob": parse(request.POST['dob']).strftime('%m/%d/%Y'),
   			"age":  calculate_age(parse(request.POST['dob'])),
			"country": request.POST['country']
		}

		if len(request.FILES) != 0:
			content['photo'] = request.FILES['photo'].read()
		db.update_one({"username": username}, {"$set": content})
		
		return redirect('profile', username=username)

def logout(request):
    del request.session['auth']
    del request.session['username']
    return redirect('home')

