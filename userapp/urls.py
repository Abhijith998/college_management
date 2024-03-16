
from userapp import views
from django.urls import path


urlpatterns = [
    path('',views.home,name='home'),
    path('student',views.student,name='student'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('logout_app',views.logout_app,name='logout_app'),
    path('profile',views.profile,name='profile'),
    path('events_user',views.events_user,name='events_user'),
    path('my_gallary',views.my_gallary,name='my_gallary'),
    path('home_user',views.home_user,name='home_user'),
    path('teacher_log',views.teacher_log,name='teacher_log'),
    path('forgotpassword/<uidb64>/<token>/',views.forgotpassword, name='forgotpassword'),
    path('email',views.email,name='email'),
    path('pin_code',views.pin_code,name='pin_code'),
    path('profile_user',views.profile_user,name='profile_user'),
    path('new_events',views.new_events,name='new_events'),
    path('user_gallary',views.user_gallary,name='user_gallary'),
    path('educational_background',views.educational_background,name='educational_background'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('update/<int:pk>',views.update,name='update'),
    
    
    
    
]