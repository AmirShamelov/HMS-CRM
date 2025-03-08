from django.shortcuts import render
from rest_framework import viewsets

from .models import Doctor
from .serializers import DoctorListSerializer

class DoctorList(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer

    def get_queryset(self):
        return self.queryset.all()


