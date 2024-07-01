from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_email_id(self, value):
        if not value.endswith('@akgec.ac.in'):
            raise serializers.ValidationError("Email must end with @akgec.ac.in")
        return value
