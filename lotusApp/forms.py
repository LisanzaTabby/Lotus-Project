from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import NumberInput

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'studentName': forms.TextInput(attrs={'class': 'form-control'}),
            'dateofbirth':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            'backgroundInfo': forms.Textarea(attrs={'rows':5,'class': 'form-control'}),
            'profilePic': forms.FileInput(attrs={'class': 'form-control'}),
            'intermediary': forms.Select(attrs={'class': 'form-control'}),
            'donor': forms.Select(attrs={'class': 'form-control'}),
            'class_level': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'primary_school': forms.Select(attrs={'class': 'form-control'}),
            'secondary_school': forms.Select(attrs={'class': 'form-control'}),
            'tertiary_school': forms.Select(attrs={'class': 'form-control'}),
            'modeofstudy': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'studentName': 'Student Name',
            'dateofbirth': 'Date of Birth',
            'gender': 'Gender',
            'backgroundInfo': 'Background Information',
            'profilePic': 'Profile Picture',
            'intermediary': 'Intermediary',
            'donor': 'Donor',
            'class_level': 'Class Level',
            'position': 'Position',
            'status': 'Status',
            'level': 'Level',
            'primary_school': 'Primary School',
            'secondary_school': 'Secondary School',
            'tertiary_school': 'Tertiary School',
            'modeofstudy': 'Mode of Study',
        }
class intermediaryForm(ModelForm):
    class Meta:
        model = Intermediary
        fields = '__all__'
        widgets = {
        'intermediaryName': forms.TextInput(attrs={'class': 'form-control'}),
        'intermediaryEmail': forms.EmailInput(attrs={'class': 'form-control'}),
        'intermediaryPhone': forms.TextInput(attrs={'class': 'form-control'}),
        'contactPerson': forms.TextInput(attrs={'class': 'form-control'}),
        'location': forms.Select(attrs={'class': 'form-control'}),
    }
    labels = {
        'intermediaryName': 'Intermediary Name',
        'intermediaryEmail': 'Intermediary Email',
        'intermediaryPhone': 'Intermediary Phone',
        'contactPerson': 'Contact Person',
        'location': 'Location',
    }

class schoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'        
        widgets = {
            'schoolName': forms.TextInput(attrs={'class': 'form-control'}),
            'schoolEmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'schoolPhone': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }   
        labels = {
            'schoolName': 'School Name',
            'schoolEmail': 'School Email',
            'schoolPhone': 'School Phone',
            'level': 'Level',
            'phone': 'Phone',
            'location': 'Location',
        }
class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        widgets = {
            'donorName': forms.TextInput(attrs={'class': 'form-control'}),
            'donorEmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'donorPhone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'donorName': 'Donor Name',
            'donorEmail': 'Donor Email',
            'donorPhone': 'Donor Phone',
            'gender': 'Gender',
        }
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'employeeName': forms.TextInput(attrs={'class': 'form-control'}),
            'employeeEmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'employeePhone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'employeeName': 'Employee Name',
            'employeeEmail': 'Employee Email',
            'employeePhone': 'Employee Phone',
            'gender': 'Gender',
            'department': 'Department',
        }
class ExamResultForm(ModelForm):
    class Meta:
        model = ExamResults
        fields = '__all__'
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'term': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'}),
            'mean_grade': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'student': 'Student',
            'term': 'Term',
            'subject': 'Subject',
            'score': 'Score',
            'mean_grade': 'Mean Grade',
        }
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'term': forms.Select(attrs={'class': 'form-control'}),
        }
