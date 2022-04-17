from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'users/home.html')

def about(request):
    return render(request,'users/about.html')

def signup(request):
    return render(request,'users/signup.html')

def login(request):
    return render(request,'users/login.html')