from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def ent_reg(request):
    return render(request, "ent_reg.html")

def registration(request):
    return render(request, "registration.html")