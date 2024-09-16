from django.shortcuts import get_object_or_404, render, redirect
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
        form = StudentForm(request.POST, request.FILES)
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
def edit_student(request,pk):
    student = get_object_or_404(Student, id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Updated Successfully')
            return redirect('student_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_student.html', {'form': form})
    return render(request, 'add_templates/add_student.html', {'form': form})
def delete_student(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student Deleted Successfully')  
        return redirect('student_list') 
    context = {'student': student}
    return render(request, 'delete_templates/student_delete.html', context)
def edit_intermediary(request,pk):
    intermediary = get_object_or_404(Intermediary, id=pk)
    form = intermediaryForm(instance=intermediary)
    if request.method == 'POST':
        form = intermediaryForm(request.POST, instance=intermediary)
        if form.is_valid():
            form.save()
            messages.success(request, 'Intermediary Updated Successfully')
            return redirect('intermediary_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_intermediary.html', {'form': form})
    context = {'form': form}
    return render(request, 'add_templates/add_intermediary.html', context)
def delete_intermediary(request,pk):
    intermediary = get_object_or_404(Intermediary, pk=pk)
    if request.method == 'POST':
        intermediary.delete()
        messages.success(request, 'Intermediary Deleted Successfully')  
        return redirect('intermediary_list') 
    context = {'intermediary': intermediary}
    return render(request, 'delete_templates/intermediary_delete.html', context)
def edit_school(request,pk):
    school = get_object_or_404(School, id=pk)
    form = schoolForm(instance=school)
    if request.method == 'POST':
        form = schoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, 'School Updated Successfully')
            return redirect('school_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_school.html', {'form': form})
    context = {'form':form}
    return render(request, 'add_templates/add_school.html', context)
def delete_school(request,pk):
    school = get_object_or_404(School, id=pk)
    if request.method == 'POST':
        school.delete()
        messages.success(request, 'School Deleted Successfully')  
        return redirect('school_list') 
    context = {'school': school}    
    return render(request, 'delete_templates/school_delete.html', context)
#data lists
def student_list(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'lists/student_list.html', {'students': students})
def intermediary_list(request):
    intermediaries = Intermediary.objects.all().order_by('id')
    return render(request, 'lists/intermediary_list.html', {'intermediaries': intermediaries})
def school_list(request):
    schools = School.objects.all().order_by('id')
    return render(request, 'lists/school_list.html', {'schools': schools})
# Finance views
def finance_view(request):
    context = {}
    return render(request, 'userpages/finance.html', context)
def donor_list(request):
    donors = Donor.objects.all().order_by('id')
    context = {'donors':donors}
    return render(request, 'lists/donor_list.html', context)
def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donor Added Successfully!')
            return redirect('donor_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_donor.html', {'form':form})
    form = DonorForm()
    return render(request, 'add_templates/add_donor.html', {'form':form})
def edit_donor(request, pk):
    donor = get_object_or_404(Donor, id=pk)
    form = DonorForm(instance=donor)
    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            messages.success(request, "Donor Information Updated Successfully")
            return redirect('donor_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_donor.html', {'form':form})
    context = {'form': form}
    return render(request, 'add_templates/add_donor.html', context)
def delete_donor(request, pk):
    donor =get_object_or_404(Donor, id=pk)
    if request.method == 'POST':
        donor.delete()
        messages.success(request, 'Donor Deleted Successfully!')
    context = {'donor':donor}
    return render(request, 'delete_templates/donor_delete.html', context)

def employee_list(request):
    employees = Employee.objects.all().order_by('id')
    context={'employees':employees}
    return render(request, 'lists/employee_list.html', context)
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Added Successfully!')
            return redirect('employee_list')
        else:
            messages.error(request, form.errorse)
            return render(request, 'add_templates/add_donor.html', {'form':form})
    form = EmployeeForm()
    return render(request, 'add_templates/add_employee.html', {'form':form})
def edit_employee(request,pk):
    employee = get_object_or_404(Employee, id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request,'Employee Information Updated Successfully!')
            return redirect('employee_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_employee.html', {'form':form})
    context = {'form':form}
    return render(request, 'add_templates/add_employee.html', context)
def delete_employee(request,pk):
    employee = get_object_or_404(Employee, id=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee Deleted Successfully!')
        return redirect(employee_list)
    context = {'employee':employee}
    return render(request, 'delete_templates/employee_delete.html', context)    
def logout_view(request):
    logout(request)
    return redirect('index')
