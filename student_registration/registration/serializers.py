# serializers.py
from rest_framework import serializers
from .models import Student
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class StudentSerializer(serializers.ModelSerializer):
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = Student
        fields = '__all__'

    def validate_email_id(self, value):
        if not value.endswith('@akgec.ac.in'):
            raise serializers.ValidationError("Email must end with @akgec.ac.in")
        return value
