from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from collegeapp.models import addcourse, students

def home(request):
    return render(request,'home.html')


def student(request):
    
    return render(request,'student.html')

def studentlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('login_password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('studentdetails')
        else:
           
            # Handle the case when authentication fails
            error_message = "Invalid username or password. Please try again."
            return render(request, 'studentlogin.html', {'error_message': error_message})

    return render(request, 'studentlogin.html')

def studentdetails(request):
    return render(request,'studentdetails.html')