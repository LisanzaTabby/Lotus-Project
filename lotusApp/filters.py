import django_filters
from .models import *
from django_filters import FilterSet

class StudentFilter(django_filters.FilterSet):
    intermediaries = django_filters.ModelMultipleChoiceFilter(queryset=Intermediary.objects.all(), label='Intermediaries')
    primary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Primary School')
    class Meta:
        model = Student
        fields =['gender']