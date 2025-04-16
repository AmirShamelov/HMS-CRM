from rest_framework import serializers

from .models import Appointment
from doctor.serializers import DoctorListSerializer
from user_profile.serializers import UserSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorListSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Appointment
        read_only_fields = (
            'created_at',
        ),

        fields = (
            'id',
            'patient_name',
            'patient_iin',
            'date',
            'time',
            'comment',
            'conclusion',
            'treatment',
            'doctor',
            'department',
            'created_by',
        )
