from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Donor(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  
    donorName = models.CharField(max_length=100, null=True, blank=True)
    donorEmail = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    donorPhone = models.CharField(max_length =100, null=True, blank=True, unique=True)
    gender = models.CharField(max_length=100, choices=GENDER, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f'{self.donorName}'
class School(models.Model):
    LEVEL=(
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('Tertiary', 'Tertiary'),
    )
    LOCATION = (
        ('Nairobi', 'Nairobi'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
        ('Eldoret', 'Eldoret'),
        ('Kitale', 'Kitale'),
        ('Kakamega', 'Kakamega'),
        ('Kitui', 'Kitui'),
        ('Nakuru', 'Nakuru'),
        ('Kilifi', 'Kilifi'),
        ('Limuru', 'Limuru'),
        ('Migori', 'Migori'),
        ('Kiambu', 'Kiambu'),
    )
    schoolName = models.CharField(max_length=100, null=True, blank=True)
    schoolEmail = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    schoolPhone = models.CharField(max_length =100, null=True, blank=True, unique=True)
    location = models.CharField(max_length=100, choices=LOCATION, null=True, blank=True)
    level = models.CharField(max_length=100, choices=LEVEL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f'{self.schoolName}'

class Intermediary(models.Model):
    LOCATION = (
        ('Nairobi', 'Nairobi'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
        ('Eldoret', 'Eldoret'),
        ('Kitale', 'Kitale'),
        ('Kakamega', 'Kakamega'),
        ('Kitui', 'Kitui'),
        ('Nakuru', 'Nakuru'),
        ('Kilifi', 'Kilifi'),
        ('Limuru', 'Limuru'),
        ('Migori', 'Migori'),
        ('Kiambu', 'Kiambu'),
    )
    intermediaryName = models.CharField(max_length=100, null=True, blank=True)
    intermediaryEmail = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    intermediaryPhone = models.CharField(max_length =100, null=True, blank=True, unique=True)
    contactPerson = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, choices=LOCATION, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f'{self.intermediaryName}'
class Student(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    ModeofStudy = (
        ('8-4-4', '8-4-4'),
        ('8-4-4-Disabled', '8-4-4-Disabled'),
        ('CBC', 'CBC'),
        ('CBC-Disabled', 'CBC-Disabled'),
    )
    LEVELofSUPPORT = (
        ('PrimaryOnly', 'PrimaryOnly'),
        ('Primary&Secondary', 'Primary&Secondary'),
        ('Primary&Secondary&Tertiary', 'Primary&Secondary&Tertiary'),
        ('Secondary&tertiary', 'Secondary&tertiary'),
        ('TertiaryOnly', 'TertiaryOnly'),
        ('SecondaryOnly', 'SecondaryOnly'),
        ('Primary&Tertiary', 'Primary&Tertiary'),
    )
    POSITION = (
        ('Continuing', 'Continuing'),
        ('Graduate', 'Graduate'),
        ('Undergraduate', 'Undergraduate'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    )
    STATUS = (
        ('Single-Orphan', 'Single-Orphan'),
        ('Double-Orphan', 'Double-Orphan'),
        ('Disadvantaged', 'Disadvantaged'),
    )
    studentName = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER, null=False)
    dateofbirth = models.DateField(null=False)
    modeofstudy = models.CharField(max_length=15, choices=ModeofStudy, null=True, blank=True)
    intermediary = models.ForeignKey(Intermediary,related_name='intermediary', on_delete=models.CASCADE, null=True, blank=True)
    donor = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    class_level = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=25, choices=POSITION, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)
    level = models.CharField(max_length=100, choices=LEVELofSUPPORT, null=True, blank=True)
    backgroundInfo = models.TextField(null=True, blank=True)
    primary_school = models.ForeignKey(School, related_name='primary_students', on_delete=models.CASCADE, null=True, blank=True)
    secondary_school = models.ForeignKey(School, related_name='secondary_students', on_delete=models.CASCADE, null=True, blank=True)
    tertiary_school = models.ForeignKey(School, related_name='tertiary_students', on_delete=models.CASCADE, null=True, blank=True)
    profilePic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f'{self.studentName}'
    def save(self, *args, **kwargs):
        if self.pk:
            original_student = Student.objects.get(pk=self.pk)
            if original_student.donor != self.donor:
                StudentDonorHistory.objects.create(
                    student = self,
                    donor = original_student.donor,
                    school_level = self.class_level,
                    year = timezone.now().year,
                    changed_on = timezone.now().date()
                )
            else:
                StudentDonorHistory.objects.create(
                    student = self,
                    donor = self.donor,
                    school_level = self.class_level,
                    year = timezone.now().year,
                    changed_on = timezone.now().date()
                )
            if original_student.class_level != self.class_level:
                AcademicProgress.objects.create(
                    student = self,
                    year = timezone.now().year,
                    class_level = original_student.class_level,
                    date_added = timezone.now().date()
                )
            else:
                AcademicProgress.objects.create(
                    student = self,
                    year = timezone.now().year,
                    class_level = self.class_level,
                    date_added = timezone.now().date()
                )


        super().save(*args, **kwargs)
class StudentDonorHistory(models.Model):
    student = models.ForeignKey(Student, related_name='student_donor_history', on_delete=models.CASCADE, null=True, blank=True)
    donor = models.ForeignKey(User, related_name='student_donor', on_delete=models.CASCADE, null=True, blank=True)
    school_level = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    changed_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student.studentName}, {self.donor.username}, {self.year}'

class AcademicProgress(models.Model):
    student = models.ForeignKey(Student, related_name='academic_progress', on_delete=models.CASCADE, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    class_level = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.studentName}, {self.class_level}'

class FeeCommitment(models.Model):
    donor = models.ForeignKey(User, related_name='donor_fee_commitment', on_delete=models.CASCADE, null=True, blank=True)
    fee_amount = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.donor.username}'
class Exam(models.Model):
    LEVEL = (
        ('Term1', 'Term1'),
        ('Term2', 'Term2'),
        ('Term3', 'Term3'),
    )
    term = models.CharField(max_length=5, choices=LEVEL,null=True, blank=True)
    def __str__(self):
        return f'{self.term}'
class ExamResults(models.Model):
    student = models.ForeignKey(Student, related_name='student_exam_results', on_delete=models.CASCADE, null=True, blank=True)
    term = models.ForeignKey(Exam, related_name='term_exam_results',on_delete=models.CASCADE,null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mean_grade = models.CharField(max_length=10, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.studentName},{self.subject}, {self.score}'
class Employee(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    DEPARTMENT = (
        ('Research', 'Research'),
        ('Finance', 'Finance'),
        ('HR', 'HR'),
        ('IT', 'IT'),
        ('Data-entry', 'Data-entry'), 
    )
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE, null=True)
    employeeName = models.CharField(max_length=100)
    employeeEmail = models.EmailField(max_length=100, unique=True)
    employeePhone = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    department = models.CharField(max_length=10, choices=DEPARTMENT)
    updated_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employeeName}'


