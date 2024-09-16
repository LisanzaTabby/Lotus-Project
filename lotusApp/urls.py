from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('dataentry/', views.dataentry_view, name='dataentry'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_intermediary/', views.add_intermediary, name='add_intermediary'),
    path('add_school/', views.add_school, name='add_school'),
    path('student_list/', views.student_list, name='student_list'),
    path('intermediary_list/', views.intermediary_list, name='intermediary_list'),    
    path('school_list/', views.school_list, name='school_list'),
    path('logout/', views.logout_view, name='logout'),
]