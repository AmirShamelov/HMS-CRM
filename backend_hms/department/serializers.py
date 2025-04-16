from rest_framework import serializers

from .models import Department
from user_profile.serializers import UserSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    doctors = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'title', 'sub_title', 'link', 'doctors']

