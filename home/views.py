from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'virtualkungfuhome.html')

def create(request):
    errors = User.objects.validate(request.POST)

    if errors:
        for field, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/')


    new_user = User.objects.register(request.POST)
    request.session['user_id'] = new_user.id
    return redirect('/students')

def login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, "Invalid Email/Password", extra_tags='login')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/students')
    return redirect('/')


def logout(request):
    request.session.clear()
    
    # localhost:8000
    return redirect('/')