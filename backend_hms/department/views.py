from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Department
from .serializers import DepartmentSerializer



class DepartmentList(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('doctors__first_name', 'doctors__last_name', 'title')

    def get_queryset(self):
        return self.queryset.all()

@api_view(['GET'])
def get_my_department(request):
    department = Department.objects.filter(doctors__in=[request.user]).first()
    serializer = DepartmentSerializer(department)

    return Response(serializer.data)


