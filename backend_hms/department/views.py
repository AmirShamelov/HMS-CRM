from django.shortcuts import render


from rest_framework import viewsets


from .models import Department
from .serializers import DepartmentSerializer



class DepartmentList(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self):
        return self.queryset.all()
