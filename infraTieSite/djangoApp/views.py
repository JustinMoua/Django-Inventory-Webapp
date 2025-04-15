from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Condition, Inspection #import of Inspection class from models.py
from .forms import LoginForm #import of LoginForm class from forms.py
# Create your views here.

@login_required(login_url='loginView')  #https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.decorators.login_required
def inspectionView(request):
    # Query all rows from the Inspection table
    inspections = Inspection.objects.all()
    # "inspections" is used in inspection.html in this for loop --> {% for inspection in inspections %}
    return render(request, "inspection.html", {"inspections": inspections})

@login_required(login_url='loginView')
def conditionView(request, id):
    print("id is:", id)
    conditions = Condition.objects.all()
    return render(request, "condition.html", {"conditions": conditions})

# def inspectionView(request):
#     rows = Inspection.objects.all()
#     return render(request, "inspection.html", {"inspection": rows })

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

# logout page
def logoutView(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('HomePageView') #Login Page