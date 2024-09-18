from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Donor)
admin.site.register(School)
admin.site.register(Intermediary)
admin.site.register(Student)
admin.site.register(StudentDonorHistory)
admin.site.register(Employee)
admin.site.register(AcademicProgress)
