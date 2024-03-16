from django.db import models
from django.contrib.auth.models import User

class addcourse(models.Model):
    course=models.CharField(max_length=50)
    fees=models.IntegerField(blank=True,null=True)

class students(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    year=models.IntegerField()
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    dept=models.ForeignKey(addcourse,on_delete=models.CASCADE)
   
class teachers(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    course=models.ForeignKey(addcourse,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    
class image(models.Model):
    heading=models.CharField(max_length=100)
    discription=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images')
    

class gallary(models.Model):
    images=models.ImageField(upload_to='gallary')

class register(models.Model):
    year=models.IntegerField()
    course=models.ForeignKey(addcourse,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    


class teacher_login(models.Model):
    phonenumber=models.CharField(max_length=100)
    courses=models.ForeignKey(addcourse,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    education=models.CharField(max_length=100,blank=True,null=True)
    
   