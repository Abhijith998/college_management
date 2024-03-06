
from userapp import views
from django.urls import path


urlpatterns = [
    path('',views.home,name='home'),
   
    path('student',views.student,name='student'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('studentdetails',views.studentdetails,name='studentdetails'),
]