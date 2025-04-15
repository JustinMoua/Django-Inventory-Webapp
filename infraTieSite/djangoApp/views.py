'''
* Filename: views.py
* Author: Justin Moua
* 
* Notes:
* 
* https://docs.djangoproject.com/en/5.1/topics/http/views/
*   - Views are functions via django in Python that "takes a web request and returns a web respons".
*  
* Below are the following views:
*   inspectionView(request)
*   conditionView(request, foreignKeyId)
*   baseView(request)
*   HomePageView(request)
*   loginView(request)
*   logOutView(request)
'''


from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Condition, Inspection #import of Inspection class from models.py
from .forms import LoginForm #import of LoginForm class from forms.py
# Create your views here.

#inspectionView(request) is Called from index.html and condition.html when a user logs out or if 
#a user who is not logged in tries to access index.html or condition.html. It is also called from
#loginView(request) below via 'inspection' which goes to urls.py to call inspectionView(request).
#Used to require a user having logged in to access inspectionView. https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.decorators.login_required
@login_required(login_url='loginView')  
def inspectionView(request):
    # Query all rows from the Inspection table
    inspections = Inspection.objects.all()
    # "inspections" is used in inspection.html in this for loop --> {% for inspection in inspections %}
    return render(request, "inspection.html", {"inspections": inspections})


#Function is called from the inspection.html after a user has successfully logged in.
#Pass foreignKeyId which will be used to fetch respective rows from the Conditions table that has a foreign key which matches
#the inspection table's id.
@login_required(login_url='loginView')
def conditionView(request, foreignKeyId):
    #translates to SELECT * FROM 'Condition' WHERE Inspection_id = foreignKeyId;
    conditions = Condition.objects.filter(Inspection_id=foreignKeyId)
    #translates to SELECT * FROM Inspection WHERE id = foreignKeyId; (Note to self that the foreignKeyId IS the id grabbed from the inspections table)
    inspections = Inspection.objects.filter(id=foreignKeyId)
    return render(request, "condition.html", {"conditions": conditions, "inspections": inspections})

def baseView(request):
    return render(request, 'base.html')

def HomePageView(request):
    return render(request, 'index.html')

#Code below borrowed and built off of django documentation on how to log a user in.
#https://docs.djangoproject.com/en/5.2/topics/auth/default/#how-to-log-a-user-out
def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            print("user is:", user)
            #If user not empty
            if user is not None:
                #Login the user
                login(request, user)
                #Take them to inspection.html
                return redirect('inspection')  # This should point to your inspection page
            else:
                #Otherwise throw an error
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