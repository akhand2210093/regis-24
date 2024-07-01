from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.core.mail import send_mail

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        student = serializer.save()
        send_mail(
            'Registration Successful',
            f'Hi {student.name}, your registration is successful.',
            'your_email@gmail.com',
            [student.email_id],
            fail_silently=False,
        )

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

