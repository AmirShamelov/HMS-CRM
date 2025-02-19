from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Department

User = get_user_model()

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class DepartmentSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'title', 'sub_title', 'link', 'doctors']

