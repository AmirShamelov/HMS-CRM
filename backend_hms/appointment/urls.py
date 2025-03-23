from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AppointmentViewSet, PatientViewSet, delete_appointment

router = DefaultRouter()
router.register('appointments', AppointmentViewSet, basename='appointments')
router.register('patients', PatientViewSet, basename='patients')
urlpatterns = [
    path('appointments/delete_appointment/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    path('', include(router.urls)),
]