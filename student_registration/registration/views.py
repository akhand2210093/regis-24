from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from django.core.mail import send_mail
import requests
from django.conf import settings

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        recaptcha_response = request.data.get('recaptcha')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'error': 'Invalid reCAPTCHA. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)

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


