from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def schoolHome(request):
    context = {}
    return render(request, 'school/index.html', context)

def schoolRegister(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST["username"]
        fname = request.POST["school_name"]
        email = request.POST["school_email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # Check for errorneous inputs
        if not username.isalnum() or not len(username) > 10:
            messages.error(request, 'Your username should be alphanumeric and less than 10 characters!')
            return redirect("school_register")

        if pass1 != pass2:
            messages.error(request, 'Passwords did not match!')
            return redirect("school_register")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()

        messages.success(request, "Account created, Now you can log in to your account!")
        return redirect("school_login")
    return render(request, "school/register.html")

def schoolLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
          
            return redirect("school_home")
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect("school_login")
        
    return render(request, "school/login.html")

def schoolLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect("school_login")