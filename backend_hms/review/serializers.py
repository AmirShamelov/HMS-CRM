from rest_framework import serializers

from .models import Review
from doctor.serializers import DoctorListSerializer

class ReviewSerializer(serializers.ModelSerializer):
    doctor = DoctorListSerializer(read_only=True)
    class Meta:
        model = Review

        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'date',
            'review',
            'doctor',
            'created_at',
        )
