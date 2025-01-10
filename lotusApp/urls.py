from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('dataentry/', views.dataentry_view, name='dataentry'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_student_results/<str:pk>/', views.add_student_results, name='add_student_results'),
    path('add_intermediary/', views.add_intermediary, name='add_intermediary'),
    path('add_school/', views.add_school, name='add_school'),
    path('edit_student/<str:pk>/', views.edit_student, name='edit_student'),
    path('delete_student/<str:pk>/', views.delete_student, name='delete_student'),
    path('edit_intermediary/<str:pk>/', views.edit_intermediary, name='edit_intermediary'),
    path('delete_intermediary/<str:pk>/', views.delete_intermediary, name='delete_intermediary'),
    path('edit_school/<str:pk>/', views.edit_school, name='edit_school'),
    path('delete_school/<str:pk>/', views.delete_school, name='delete_school'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_profile/<str:pk>/', views.student_profile_view, name='student_profile'),
    path('update_exam_results/<str:pk>/', views.update_exam_results, name='update_exam_results'),
    path('intermediary_list/', views.intermediary_list, name='intermediary_list'),    
    path('school_list/', views.school_list, name='school_list'),

    path('finance/', views.finance_view, name='finance'),
    path('donor_list/', views.donor_list, name='donor_list'),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('edit_donor/<str:pk>/', views.edit_donor, name='edit_donor'),
    path('delete_donor/<str:pk>/', views.delete_donor, name='delete_donor'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<str:pk>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<str:pk>/', views.delete_employee, name='delete_employee'),

    path('donor/', views.donor_view, name='donor'),
    path('donor_specific_students/', views.donor_specific_students, name='donor_specific_students'),
    path('logout/', views.logout_view, name='logout'),
]