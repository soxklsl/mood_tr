from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse
from .models import Users

def registration(request):
    return render(request, "registration.html")

def postuser(request):
    user_login = request.POST.get("user_login", "not found")
    password = request.POST.get("user_password", "not found")
    password_salt = "nn"
    user = Users.objects.create(user_login=user_login, password=password, password_salt=password_salt)
    return HttpResponse(f"<h2>create {user.id}</h2>")

        

def main(request):
    return render(request, "main.html")

def ent_reg(request):
    return render(request, "ent_reg.html")





def entrance(request):
    return render(request, "entrance.html")