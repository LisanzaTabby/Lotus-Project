from django import forms
from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['date_added']
class intermediaryForm(ModelForm):
    class Meta:
        model = Intermediary
        fields = '__all__'
        exclude = ['date_added']
class schoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'        
        exclude = ['date_added']    
class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        exclude = ['date_added']
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['date_joined']
