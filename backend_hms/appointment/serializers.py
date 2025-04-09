from rest_framework import serializers

from .models import Appointment
from doctor.serializers import DoctorListSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorListSerializer(read_only=True)

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
            'conclusion',
            'treatment',
            'doctor',
            'department'
        )
