from django.shortcuts import render


from rest_framework import viewsets


from .models import Departments
from .serializers import DepartmentSerializer



class DepartmentList(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()

    def get_queryset(self):
        return self.queryset.all()
