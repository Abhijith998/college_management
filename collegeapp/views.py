from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import make_password

from collegeapp.models import addcourse, gallary, image, register, students, teacher_login, teachers

from collegeapp.models import addcourse
from userapp.views import student
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User

def index(request):
    # return HttpResponse('fgh')
    return render(request,'index.html')

def course(request):
    if request.method=="POST":
        courses=request.POST['course']
        fee=request.POST['fee']
        data=addcourse(course=courses,fees=fee)
        data.save()
        
    return render(request,'course.html')



def addstudent(request,):
    all_course=addcourse.objects.all()
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        course_add = request.POST['course']
        year=request.POST['year']
        email=request.POST['email']
        password=request.POST['password']
        course=addcourse.objects.get(id=course_add)
        password = make_password(password)
        if User.objects.filter(email=email).exists():
            messages.error(request,'Already Exist')
        else:
            datanames=User.objects.create(first_name=firstname,last_name=lastname,email=email,password=password,username=username,is_superuser=0)
            datanames.save()

            data=register(year=year,course=course,user=datanames)
            data.save()
            messages.success(request,'Data Saved Suceesfully')
            return redirect(request.path)
        
    return render(request,'addstudent.html',{'c':all_course})

def viewstudents(request):
    datas=students.objects.all()
    return render(request,'viewstudents.html',{'st':datas})


def delete_student(request,pk):
    dlte=students.objects.get(id=pk)
    dlte.delete()
    return redirect('viewstudents')
    

def edit_student(request,pk):
    edits=students.objects.get(id=pk)
    course=addcourse.objects.all()

    if request.method=='POST':
        edits.firstname=request.POST['firstname']
        edits.lastname=request.POST['lastname']
        course_id = request.POST['course']
        edits.dept=addcourse.objects.get(id=course_id)
        edits.year=request.POST['year']
        edits.email=request.POST['email']
        edits.password=request.POST['password']
        edits.save()
        return redirect('viewstudents')

    return render(request,'edit_student.html',{'edits':edits,'c':course})

def Teachers(request):
   
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        education=request.POST['education']
        course=request.POST['course']
        number=request.POST['number']
        password=request.POST['password']
        courses=addcourse.objects.get(id=course)
        password = make_password(password)
        if User.objects.filter(username=username).exists():
            messages.error(request,'Already Exist')
        else:
            data_user=User.objects.create(first_name=firstname,last_name=lastname,username=username,password=password,email=email)
            data_user.save()
            teacher=teacher_login(phonenumber=number,education=education,courses=courses,user=data_user)
            teacher.save()

    datas=addcourse.objects.all()
    return render(request,'Teachers.html',{'teacher':datas})
    
def delete_teacher(request,pk):
    data=teachers.objects.get(id=pk)
    data.delete()
    return redirect('viewteachers')


def edit_teachers(request,pk):
    teacher=teachers.objects.get(id=pk)
    course=addcourse.objects.all()
    if request.method=="POST":
        teacher.firstname=request.POST['firstname']
        teacher.lastname=request.POST['lastname']
        course=request.POST['course']
        teacher.course=addcourse.objects.get(id=course)
        teacher.phonenumber=request.POST['phonenumber']
        teacher.save()
        return redirect('viewteachers')
    return render(request,'edit_teachers.html',{'teac':teacher,'e':course,})  
        
       

def viewteachers(request):
    datas=teachers.objects.all()
    return render(request,'viewteachers.html',{'te':datas})

def events(request):
    return render(request,'events.html')

def viewdetails(request):
    savedata=addcourse.objects.all()
    return render(request,'viewdetails.html',{'view':savedata})

def delete(request,pk):
    data=addcourse.objects.get(id=pk)
    data.delete()
    return redirect('viewdetails')

def edit(request,pk):
    datas=addcourse.objects.get(id=pk)
    if request.method=='POST':
        datas.course=request.POST['courses']
        datas.fees=request.POST['fee']
        datas.save()
        return redirect('viewdetails')


    return render(request,'edit.html',{'edit':datas})

def viewevent(request):
    datas=image.objects.all()
    return render(request,'viewevent.html',{'datas':datas})

def addevents(request):
    
    if request.method=='POST':
        heading=request.POST['heading']
        discription=request.POST['discription']
        images=request.FILES.get('image')
        data=image(heading=heading,discription=discription,image=images)
        data.save()
        return redirect('addevents')
    return render(request,'addevents.html')

def delete_event(request,pk):
    event=image.objects.get(id=pk)
    event.delete()
    return redirect('viewevent')

def edit_event(request,pk):
    edit=image.objects.get(id=pk)
    if request.method=='POST':
        edit.heading=request.POST['heading']
        edit.discription=request.POST['discription']
        images=request.FILES.get('image')
        if images:
            edit.image=images
            edit.save()
        return redirect('viewevent')
    return render(request,'edit_event.html',{'edit':edit})

def gallarys(request):
    if request.method=="POST":
        imag=request.FILES.getlist('image')
        for i in imag:
            data=gallary(images=i)
            data.save()
    return render(request,'gallary.html')


def view_gallary(request):
    gall=gallary.objects.all()
    return render(request,'view_gallary.html',{'gall':gall})

def delete_gallary(request,pk):
    data=gallary.objects.get(id=pk)
    data.delete()
    return redirect('view_gallary')

def edit_gallary(request,pk):
    datas=gallary.objects.get(id=pk)
    if request.method=="POST":
        image=request.FILES.get('image')
        if image:
            datas.images=image
            datas.save()
        return redirect('view_gallary')
    return render(request,'edit_gallary.html',{'datas':datas})



def login_admin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            request.session['username'] = user.username

            return  redirect('index')
        else:
            return redirect('login_admin')

    return render(request,'login_admin.html')

@never_cache
def logout_user(request):
    logout(request)
    request.session.flush()
    return redirect('home')


def logout_page(request):
    return render(request,'logout_page.html')