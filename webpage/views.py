from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html",{})
def login(request):
    return render(request, "login.html",{})
def signup(request):
    return render(request, "signup.html",{})
def blog(request):
    return render(request, "blog.html",{})
def contact(request):
    return render(request, "contact.html",{})
def home(request):
    return render(request, "home.html",{})
def upload(request):
    return render(request, "upload.html",{})

