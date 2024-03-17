
import random
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from collegeapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.encoding import force_str
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode

def home(request):
    courses=addcourse.objects.all()
    images=image.objects.all()
    return render(request,'home.html',{'courses':courses,'images':images})


def student(request):
    
    return render(request,'student.html')
def studentlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('login_password')

        user = authenticate(request, username=username, password=password)
        request.session['username'] = user.username
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home_user')   
    return render(request, 'studentlogin.html')
    


@never_cache
@login_required(login_url='/studentlogin/')  # Add login_required decorator if needed
def logout_app(request):
    logout(request)
    request.session.flush()

    response = redirect('/')
    
    # Set cache-control headers to prevent caching
    response['Cache-Control'] = 'no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response

def profile(request):
    
    if request.user.is_authenticated:
        user_email = request.user.email
        user_username = request.user.username

        # Fetch details from the 'register' table for the logged-in user
        user_details = register.objects.get(user=request.user)
        
        return render(request, 'profile.html', {'user': user_details,'user_email':user_email,'user_username':user_username})
        
    else:
        # Handle the case where 'username' is not found in the session
        return render(request, 'profile.html', {'error_message': 'Username not in session'})

def events_user(request):
    data = image.objects.all()
    return render(request, 'events_user.html', {'data': data})


def my_gallary(request):
    photo=gallary.objects.all()
    return render(request,'my_gallary.html',{'photo':photo})

def home_user(request):
    if request.user.is_authenticated:
        user_username = request.user.username

        # Fetch details from the 'register' table for the logged-in user
        
        return render(request, 'home_user.html', {'user_username':user_username})
           
    else:
        # Handle the case where 'username' is not found in the session
        return render(request, 'home_user.html', {'error_message': 'Username not in session'})

def teacher_log(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        useruser = authenticate(request, username=user_name, password=password)
        print(useruser)
        if useruser is not None:
            login(request, useruser)
            request.session['username'] = useruser.username
            return redirect('profile_user')
       
           

    return render(request, 'teacher_log.html')

@never_cache
@login_required(login_url='/teacher_log/')  # Add login_required decorator if needed
def logout_user(request):
    logout(request)
    request.session.flush()

    response = redirect('teacher_log')
    
    # Set cache-control headers to prevent caching
    response['Cache-Control'] = 'no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response



def forgotpassword(request,uidb64,token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(id=uid)
    request.session['uidb64']=str(uidb64)
    request.session['token']=token
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('newpassword')
            confirm_password = request.POST.get('confirmpassword')
            
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                print( 'Your password has been successfully reset')
                return redirect('teacher_log')  # Redirect to the login page after successful password reset
            else:
                messages.error(request, 'invalid username or password')
                return redirect('forgotpassword', uidb64=uidb64, token=token)
        else:
            return render(request, 'forgotpassword.html')
           
    return render(request,'forgotpassword.html')


def email(request):
    if request.method == 'POST':
        email = request.POST['email']
        request.session['email']=email
        user = User.objects.get(email=email)
        pin = ""
        for i in range(6):
            number = random.randint(1, 9)
            pin += str(number)
            request.session['pno']=pin
        subject = 'Password Reset'
        message = f"Hello {user.username},\n\nYou recently requested to reset your password. Please type 6 digit pin  to continue with the password reset:\n{pin}\n\nIf you did not request this reset, please ignore this email.\n\nThank you!"
        send_mail(subject, message, 'nikagod95@gmail.com', [email])
        
        return redirect('pin_code')
    
    return render(request,'email.html')


def pin_code(request):
    email=request.session.get('email')
    user = User.objects.get(email=email)
    token = default_token_generator.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    
    if request.method == 'POST':
            pin_number = request.POST.get('pin_code')
            pin_session=request.session.get('pno')
           
            if pin_number == pin_session :
                reset_link = request.build_absolute_uri(reverse('forgotpassword', kwargs={'uidb64': uidb64, 'token':token}))
                return redirect(reset_link)
            else:
                return redirect('pin_code')
    return render(request,'pin_code.html')

def profile_user(request):
    if request.user.is_authenticated:
            user_email = request.user.email
            user_username = request.user.username

            # Fetch details from the 'register' table for the logged-in user
            user_details = teacher_login.objects.get(user=request.user)
           
            return render(request, 'profile_user.html', {'user': user_details,'user_email':user_email,'user_username':user_username})
            
    else:
            return render(request, 'profile_user.html', {'error_message': 'Username not in session'})
def new_events(request):
    datas=image.objects.all()
    return render(request,'new_events.html',{'event':datas})

def user_gallary(request):
    user=gallary.objects.all()
    return render(request,'user_gallary.html',{'user':user})

def educational_background(request):
    username = request.session.get('username')
    print(username)
    print('secuess')
    user = User.objects.get(username=username)
    teacher = teacher_login.objects.get(user_id=user)

            # Fetch details from the 'register' table for the logged-in user
    # user_details = teacher_login.objects.get(user=requ/est.user)
    teacher_logins = teacher_login.objects.all()  # You may filter this queryset based on your requirements

# Extracting individual education items from each teacher_login instance
    education_items = []
    for login in teacher_logins:
        if login.education:
            education_items.extend(login.education.split(','))

    return render(request, 'educational_background.html', {'teacher_logins':teacher_logins,'education_items':education_items})
def update(request, pk):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    teacher = teacher_login.objects.get(user=user)
    course = addcourse.objects.all()

    if request.method == 'POST':
        teacher.phonenumber = request.POST.get('number')
        
        # Retrieve the addcourse instance based on the provided course ID
        course_id = request.POST.get('course')
        selected_course = addcourse.objects.get(pk=course_id)
        
        # Assign the retrieved addcourse instance to the teacher's courses field
        teacher.courses = selected_course
        teacher.save()
        user.email = request.POST.get('email')
          # Save the changes
        user.save()
        return redirect('profile_user')
    
    return render(request, 'update.html', {'teacher': teacher, 'course': course})
