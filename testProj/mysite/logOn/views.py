from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Change this to your desired post-login page
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "login.html", {'form': AuthenticationForm()})

def home_view(request):
    return render(request, "home.html")

# @login_required
def logout_view(request):
    logout(request)
    return render(request, "logout.html", {})