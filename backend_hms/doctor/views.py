from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from .models import Doctor
from .serializers import DoctorListSerializer

class DoctorPagination(PageNumberPagination):
    page_size = 6

class DoctorList(viewsets.ModelViewSet):
    serializer_class = DoctorListSerializer
    queryset = Doctor.objects.all().order_by('id')
    pagination_class = DoctorPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('position', 'doctor__first_name', 'doctor__last_name')

    def get_queryset(self):
        return self.queryset.all()


