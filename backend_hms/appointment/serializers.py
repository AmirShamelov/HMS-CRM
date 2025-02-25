from rest_framework import serializers

from .models import Appointment
from department.serializers import DoctorSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Appointment
        read_only_fields = (
            'created_by',
            'created_at',
        ),

        fields = (
            'id',
            'patient_name',
            'patient_iin',
            'date',
            'time',
            'comment',
            'doctor',
            'department'
        )