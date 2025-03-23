from django.contrib.auth.models import User
from rest_framework import viewsets, filters, pagination, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

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


    @action(detail=False, methods=['get'])
    def available_dates(self, request):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:

            from datetime import date, timedelta
            from time import time

            start_date = date.fromtimestamp(time())
            end_date = start_date + timedelta(days=7)
            all_dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

            filtered_dates = [d for d in all_dates if d.weekday() < 5]

            return Response([d.isoformat() for d in filtered_dates])
        return Response()


    @action(detail=False, methods=['get'])
    def available_times(self, request):
        doctor_id = request.query_params.get('doctor_id')
        date = request.query_params.get('date')
        if doctor_id and date:
            booked_times = Appointment.objects.filter(doctor_id=doctor_id, date=date).values_list('time', flat=True)

            available_times = [time for time in Appointment.TIME_CHOICES if time[0] not in booked_times]
            return Response(available_times)
        return Response([])

@api_view(['POST'])
def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.delete()

    return Response({'message': 'The appointment was deleted'})

class PatientPagination(PageNumberPagination):
    page_size = 4

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all().order_by('-id')
    pagination_class = PatientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('patient_name', 'patient_iin')

    def get_queryset(self):
        return self.queryset.filter(doctor=self.request.user)





