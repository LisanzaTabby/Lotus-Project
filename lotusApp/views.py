from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dataentry')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
    return render(request, 'login.html')
def dataentry_view(request):
    context = {}
    return render(request, 'userpages/dataentry.html', context)
# dataentry actions
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Added Successfully')
            return redirect('student_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_student.html')

    form = StudentForm()
    return render(request, 'add_templates/add_student.html', {'form': form})
def add_intermediary(request):
    if request.method == 'POST':
        form = intermediaryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Intermediary Added Successfully')
            return redirect('intermediary_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_intermediary.html')
    form = intermediaryForm()
    return render(request, 'add_templates/add_intermediary.html', {'form': form})
def add_school(request):
    if request.method == 'POST':
        form = schoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'School Added Successfully')
            return redirect('school_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_school.html')
    form = schoolForm()    
    return render(request, 'add_templates/add_school.html', {'form': form})
#data lists
def student_list(request):
    students = Student.objects.all()
    return render(request, 'lists/student_list.html', {'students': students})
def intermediary_list(request):
    intermediaries = Intermediary.objects.all()
    return render(request, 'lists/intermediary_list.html', {'intermediaries': intermediaries})
def school_list(request):
    schools = School.objects.all()
    return render(request, 'lists/school_list.html', {'schools': schools})


def logout_view(request):
    logout(request)
    return redirect('index')
