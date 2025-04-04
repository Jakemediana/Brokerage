from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    context = {}
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.user.is_superuser:
                return redirect('/home')
            else:
                context["message"] = "Welcome to Grancho Customs Brokerage!"
                return redirect('/home')
        else:
            context["message"] = "Invalid credentials!"
            return render(request, "login.html", context)
    else:
        if request.user.is_authenticated:
            return redirect('/home')
        else:
            return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect('/')

#@login_required()
def home(request):
    context = {}
    context["message"] = "Welcome " + request.user.first_name + " " + request.user.last_name + "!"
    return render(request, "home.html", context)