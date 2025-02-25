from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from department.models import Department
from .models import Appointment

from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def perform_create(self, serializer):
        doctor_id = self.request.data['doctor_id']

        user = User.objects.get(pk=doctor_id)

        serializer.save(doctor=user, created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
