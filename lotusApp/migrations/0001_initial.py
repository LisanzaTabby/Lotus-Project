# Generated by Django 5.1.1 on 2024-09-16 06:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intermediary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intermediaryName', models.CharField(blank=True, max_length=100, null=True)),
                ('intermediaryEmail', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('intermediaryPhone', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('contactPerson', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Eldoret', 'Eldoret'), ('Kitale', 'Kitale'), ('Kakamega', 'Kakamega'), ('Kitui', 'Kitui'), ('Nakuru', 'Nakuru'), ('Kilifi', 'Kilifi'), ('Limuru', 'Limuru'), ('Migori', 'Migori'), ('Kiambu', 'Kiambu')], max_length=100, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(blank=True, max_length=100, null=True)),
                ('schoolEmail', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('schoolPhone', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('location', models.CharField(blank=True, choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Eldoret', 'Eldoret'), ('Kitale', 'Kitale'), ('Kakamega', 'Kakamega'), ('Kitui', 'Kitui'), ('Nakuru', 'Nakuru'), ('Kilifi', 'Kilifi'), ('Limuru', 'Limuru'), ('Migori', 'Migori'), ('Kiambu', 'Kiambu')], max_length=100, null=True)),
                ('level', models.CharField(blank=True, choices=[('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Tertiary', 'Tertiary')], max_length=100, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donorName', models.CharField(blank=True, max_length=100, null=True)),
                ('donorEmail', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('donorPhone', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10)),
                ('dateofbirth', models.DateField()),
                ('modeofstudy', models.CharField(blank=True, choices=[('8-4-4', '8-4-4'), ('8-4-4-Disabled', '8-4-4-Disabled'), ('CBC', 'CBC'), ('CBC-Disabled', 'CBC-Disabled')], max_length=15, null=True)),
                ('class_level', models.CharField(blank=True, max_length=20, null=True)),
                ('position', models.CharField(blank=True, choices=[('Continuing', 'Continuing'), ('Graduate', 'Graduate'), ('Undergraduate', 'Undergraduate'), ('Completed', 'Completed'), ('Discontinued', 'Discontinued')], max_length=25, null=True)),
                ('status', models.CharField(blank=True, choices=[('Single-Orphan', 'Single-Orphan'), ('Double-Orphan', 'Double-Orphan'), ('Disadvantaged', 'Disadvantaged')], max_length=20, null=True)),
                ('level', models.CharField(blank=True, choices=[('PrimaryOnly', 'PrimaryOnly'), ('Primary&Secondary', 'Primary&Secondary'), ('Primary&Secondary&Tertiary', 'Primary&Secondary&Tertiary'), ('Secondary&tertiary', 'Secondary&tertiary'), ('TertiaryOnly', 'TertiaryOnly'), ('SecondaryOnly', 'SecondaryOnly'), ('Primary&Tertiary', 'Primary&Tertiary')], max_length=100, null=True)),
                ('backgroundInfo', models.TextField(blank=True, null=True)),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('intermediary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intermediary', to='lotusApp.intermediary')),
                ('primary_school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_students', to='lotusApp.school')),
                ('secondary_school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_students', to='lotusApp.school')),
                ('tertiary_school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tertiary_students', to='lotusApp.school')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDonorHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_level', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('changed_on', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_donor', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_donor_history', to='lotusApp.student')),
            ],
        ),
    ]