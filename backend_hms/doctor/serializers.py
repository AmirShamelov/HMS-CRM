from rest_framework import serializers

from .models import Doctor
from department.serializers import DepartmentSerializer, UserSerializer


class DoctorListSerializer(serializers.ModelSerializer):
    doctor = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = (
            'id',
            'doctor',
            'full_name',
            'department',
            'education',
            'position',
            'get_image',
            'description',
            'email',
            'phone'
        )

    def get_full_name(self, obj):
        return f"{obj.doctor.first_name} {obj.doctor.last_name}"




