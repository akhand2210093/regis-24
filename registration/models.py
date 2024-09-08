# models.py
from django.db import models
from django.core.exceptions import ValidationError

def validate_email(value):
    if not value.endswith('@akgec.ac.in'):
        raise ValidationError("Email must end with @akgec.ac.in")

class Student(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    branch = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    student_no = models.CharField(max_length=20, unique=True)
    email_id = models.EmailField(unique=True, validators=[validate_email])
    phone_no = models.CharField(max_length=15, unique=True)
    residence = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)

    def __str__(self):
        return self.email_id
