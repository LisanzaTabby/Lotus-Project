from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .forms import *
from .decorators import unauthenticated_user, allowed_users
from .filters import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.groups.filter(name='Dataentry').exists():
                login(request, user)
                return redirect('dataentry')
            elif user.groups.filter(name='Finance').exists():
                login(request, user)
                return redirect('finance')
            elif user.groups.filter(name='Donor').exists():
                login(request, user)
                return redirect('donor')
            else:
                return HttpResponse('You are not an Authorized User!')
        else:
            messages.error(request, 'Invalid Credentials, try Again')
            return render(request, 'login.html') 
    return render(request, 'login.html')
@login_required
def student_profile_view(request, pk):
    student = get_object_or_404(Student, id=pk)
    academicprogress = AcademicProgress.objects.filter(student=student).order_by('-year')
    donor_history = StudentDonorHistory.objects.filter(student=student).order_by('-year')
    is_dataentry = request.user.groups.filter(name='Dataentry').exists()
    is_finance = request.user.groups.filter(name='Finance').exists()
    is_donor = request.user.groups.filter(name='Donor').exists()
    context = {'student': student,'donor_history':donor_history, 'is_dataentry':is_dataentry,'is_finance':is_finance, 'is_donor':is_donor,'academicprogress':academicprogress}  
    return render(request, 'profiles/student_profile.html', context)
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def dataentry_view(request):
    students = Student.objects.all()
    intermediaries = Intermediary.objects.all()
    schools = School.objects.all()

    students_count = students.count()
    intermediaries_count = intermediaries.count()
    schools_count = schools.count()
    
    context = {'students':students,'intermediaries':intermediaries,'schools':schools,'students_count':students_count,'intermediaries_count':intermediaries_count,'schools_count':schools_count}
    return render(request, 'userpages/dataentry.html', context)
# dataentry actions
@login_required
@allowed_users(allowed_roles=['Dataentry'])
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
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def add_student_results(request,pk):
    student = get_object_or_404(Student, id=pk)
    ResultsFormSet = inlineformset_factory(Student, ExamResults, form=ExamForm, fields=('subject','score','mean_grade'), extra=5)
    termform= ExamForm(request.POST or None)
    ResultsForm = ResultsFormSet(queryset=ExamResults.objects.none(), instance=student)
    if request.method == 'POST':
        termform = ExamForm(request.POST)
        ResultsForm = ResultsFormSet(request.POST, instance=student)
        if termform.is_valid() and ResultsForm.is_valid():
             terminstance = termform.save()
             for form in ResultsForm:
                 result = form.save(commit=False)
                 result.term = terminstance.term
                 result.save()
        messages.success(request, 'Results and term added successfully')
        return redirect('student_profile', pk=pk)
    else:
        messages.error(request, 'There was an error with your submission.')
        for form in ResultsForm:
            for field in form.errors:
                messages.error(request, f"{field}: {form.errors[field]}")
    context = {
        'termform': termform,
        'ResultsForm': ResultsForm,
    }
    
    return render(request, 'add_templates/add_student_results.html', context)
@login_required
@allowed_users(allowed_roles=['Dataentry'])
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
@login_required
@allowed_users(allowed_roles=['Dataentry'])
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
@login_required
@allowed_users(allowed_roles=['Dataentry'])
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
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def delete_student(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student Deleted Successfully')  
        return redirect('student_list') 
    context = {'student': student}
    return render(request, 'delete_templates/student_delete.html', context)
@login_required
@allowed_users(allowed_roles=['Dataentry'])
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
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def delete_intermediary(request,pk):
    intermediary = get_object_or_404(Intermediary, pk=pk)
    if request.method == 'POST':
        intermediary.delete()
        messages.success(request, 'Intermediary Deleted Successfully')  
        return redirect('intermediary_list') 
    context = {'intermediary': intermediary}
    return render(request, 'delete_templates/intermediary_delete.html', context)
@login_required
@allowed_users(allowed_roles=['Dataentry'])
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
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def delete_school(request,pk):
    school = get_object_or_404(School, id=pk)
    if request.method == 'POST':
        school.delete()
        messages.success(request, 'School Deleted Successfully')  
        return redirect('school_list') 
    context = {'school': school}    
    return render(request, 'delete_templates/school_delete.html', context)
#data lists
@login_required
@allowed_users(allowed_roles=['Dataentry','Finance'])
def student_list(request):
    students = Student.objects.all().order_by('id')
    myFilter = StudentFilter(request.POST, queryset=students)
    students = myFilter.qs
    is_dataentry = request.user.groups.filter(name='Dataentry').exists()
    is_finance = request.user.groups.filter(name='Finance').exists()
    is_donor = request.user.groups.filter(name='Donor').exists()
    return render(request, 'lists/student_list.html', {'students': students,'is_dataentry':is_dataentry,'is_finance':is_finance,'is_donor':is_donor, 'myFilter':myFilter})
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def intermediary_list(request):
    intermediaries = Intermediary.objects.all().order_by('id')
    myFilter = IntermediaryFilter(request.POST, queryset = intermediaries)
    intermediaries = myFilter.qs
    return render(request, 'lists/intermediary_list.html', {'intermediaries': intermediaries,'myFilter':myFilter})
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def school_list(request):
    schools = School.objects.all().order_by('id')
    myFilter = SchoolFilter(request.POST, queryset=schools)
    schools = myFilter.qs
    return render(request, 'lists/school_list.html', {'schools': schools, 'myFilter':myFilter})

# Finance views
@login_required
@allowed_users(allowed_roles=['Finance'])
def finance_view(request):
    students = Student.objects.all()
    student_count = students.count()

    donors = Donor.objects.all()
    donor_count = donors.count()

    employees = Employee.objects.all()
    employee_count = employees.count()

    context = {'students':students,'student_count':student_count,'donors':donors,'donor_count':donor_count,'employees':employees,'employee_count':employee_count}   
    return render(request, 'userpages/finance.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
def donor_list(request):
    donors = Donor.objects.all().order_by('id')
    myFilter = DonorFilter(request.GET, queryset=donors)
    donors = myFilter.qs
    context = {'donors':donors,'myFilter':myFilter}
    return render(request, 'lists/donor_list.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
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
@login_required
@allowed_users(allowed_roles=['Finance'])
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
@login_required
@allowed_users(allowed_roles=['Finance'])
def delete_donor(request, pk):
    donor =get_object_or_404(Donor, id=pk)
    if request.method == 'POST':
        donor.delete()
        messages.success(request, 'Donor Deleted Successfully!')
    context = {'donor':donor}
    return render(request, 'delete_templates/donor_delete.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
def employee_list(request):
    employees = Employee.objects.all().order_by('id')
    myFilter = EmployeeFilter(request.GET, queryset=employees)
    employees = myFilter.qs
    context={'employees':employees,'myFilter':myFilter}
    return render(request, 'lists/employee_list.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Added Successfully!')
            return redirect('employee_list')
        else:
            messages.error(request, form.errors)
            return render(request, 'lists/employee_list.html', {'form':form})
    form = EmployeeForm()
    return render(request, 'add_templates/add_employee.html', {'form':form})
@login_required
@allowed_users(allowed_roles=['Finance'])
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
@login_required
@allowed_users(allowed_roles=['Finance'])
def delete_employee(request,pk):
    employee = get_object_or_404(Employee, id=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee Deleted Successfully!')
        return redirect(employee_list)
    context = {'employee':employee}
    return render(request, 'delete_templates/employee_delete.html', context) 
@login_required
@allowed_users(allowed_roles=['Donor'])
def donor_view(request):
    students = Student.objects.filter(donor=request.user)
    student_count = students.count()
    context = {'students':students, 'student_count':student_count}
    return render(request, 'userpages/donor.html', context)
@login_required
@allowed_users(allowed_roles=['Donor'])
def donor_specific_students(request):
    students = Student.objects.select_related('donor').filter(donor=request.user)
    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs
    context = {'students':students, 'myFilter':myFilter}
    return render (request, 'lists/donor_specific_students.html', context)
def logout_view(request):
    logout(request)
    return redirect('index')
