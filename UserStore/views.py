from django.shortcuts import render, redirect
from .models import BookModel, Cart, CartItem
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.http import JsonResponse
# Create your views here.
def home_view(req):
    return render(req, "home.html")

def login_view(req):
    return render(req, "login.html")

def sign_in_view(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            print("User is created")
            return redirect("login")
        else:
            print("Form is not valid from sign_in_view")
    else:
        form = UserCreationForm()
        print("Error")
    return render(req, "sign_in.html", {'form':form})

@login_required
def store_view(req):
    books = BookModel.objects.all()
    for book in books:
        print(books)
    return render(req, "store.html", {"books":books})

def user_login_view(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect("store")
            else:
                form.add_error(None, "Invalid Username or Password")
        else:
            form.add_error(None, "Form is not valid")

    
    else:
        
        form = AuthenticationForm()
    return render(req, "login.html", {"form":form})

def logout_view(req):
    logout(req)
    return redirect("home")

