
from collegeapp import views
from django.urls import path


urlpatterns = [
    path('index',views.index,name='index'),
    path('course',views.course,name='course'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('Teachers',views.Teachers,name='Teachers'),
    path('events',views.events,name='events'),
    path('viewdetails',views.viewdetails,name='viewdetails'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('viewdetails',views.viewdetails,name='viewdetails'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path('edit_student/<int:pk>',views.edit_student,name='edit_student'),
    path('delete_teacher/<int:pk>',views.delete_teacher,name='delete_teacher'),
    path('viewteachers',views.viewteachers,name='viewteachers'),
    path('edit_teachers/<int:pk>',views.edit_teachers,name='edit_teachers'),
    path('delete_event/<int:pk>',views.delete_event,name='delete_event'),
    path('viewevent',views.viewevent,name='viewevent'),
    path('addevents',views.addevents,name='addevents'),
    path('edit_event/<int:pk>',views.edit_event,name='edit_event'),
    path('gallarys',views.gallarys,name='gallarys'),
    path('view_gallary',views.view_gallary,name='view_gallary'),
    path('delete_gallary/<int:pk>',views.delete_gallary,name='delete_gallary'),
    path('edit_gallary/<int:pk>',views.edit_gallary,name='edit_gallary'),
     path('login_admin',views.login_admin,name='login_admin'),
    path('logout_user',views.logout_user,name='logout_user'),
]