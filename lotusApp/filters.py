import django_filters
from .models import *
from django_filters import FilterSet

class StudentFilter(django_filters.FilterSet):
    studentName = django_filters.CharFilter(lookup_expr='icontains', label='Student Name')
    donor = django_filters.ModelChoiceFilter(queryset=User.objects.all(), label='Donor')
    intermediaries = django_filters.ModelChoiceFilter(queryset=Intermediary.objects.all(), label='Intermediaries')
    primary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Primary School')
    secondary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Secondary School')
    tertiary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Tertiary School')
    class Meta:
        model = Student
        fields = ['gender']

class DonorFilter(django_filters.FilterSet):
    class Meta:
        model = Donor
        fields = ['donorName', 'gender']

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['employeeName','department', 'gender']

class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ['schoolName', 'level', 'location']
class IntermediaryFilter(django_filters.FilterSet):
    class Meta:
        model = Intermediary
        fields = ['intermediaryName', 'location']


      