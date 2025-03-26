from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Review
from doctor.models import Doctor

from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        doctor_id = self.request.data['doctor_id']

        doctor = Doctor.objects.get(pk=doctor_id)

        serializer.save(doctor=doctor)

    def get_queryset(self):
        doctor_id = self.request.query_params.get('doctor_id')

        return self.queryset.filter(doctor_id=doctor_id)
