from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
        if not username.isalnum() or len(username) > 10:
            return redirect("school_home")

        if pass1 != pass2:
            return redirect("school_home")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()

        return redirect("school_home")
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
            return redirect("school_home")
        
    return render(request, "school/login.html")