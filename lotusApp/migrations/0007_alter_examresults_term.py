# Generated by Django 5.1.1 on 2025-01-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotusApp', '0006_academicprogress_updated_at_employee_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examresults',
            name='term',
            field=models.CharField(blank=True, choices=[('Term1', 'Term1'), ('Term2', 'Term2'), ('Term3', 'Term3')], max_length=5, null=True),
        ),
    ]
