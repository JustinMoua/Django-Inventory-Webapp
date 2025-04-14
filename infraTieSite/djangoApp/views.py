from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Inspection #import of Inspection class from models.py
from .forms import LoginForm #import of LoginForm class from forms.py
# Create your views here.

def inspection_view(request):
    # Query all rows from the Inspection table
    inspections = Inspection.objects.all()
    return render(request, "inspection.html", {"inspections": inspections})

def baseView(request):
    return render(request, 'base.html')

def HomePageView(request):
    return render(request, 'index.html')

def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            print("user is:", user)
            if user is not None:
                login(request, user)
                return redirect('inspection')  # This should point to your inspection page
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('HomePageView')  # Redirect back to login page
        else:
            messages.error(request, "form not valid.")
            return redirect('HomePageView')  # Redirect back to login page
    else:
        form = LoginForm()
        return redirect('HomePageView')  # If someone visits the login view directly

def inspectionView(request):
    rows = Inspection.objects.all()
    return render(request, "inspection.html", {"inspection": rows })

# logout page
def user_logout(request):
    logout(request)
    return redirect('HomePageView') #Login Page