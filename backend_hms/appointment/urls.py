from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AppointmentViewSet, PatientViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet, basename='appointments')
router.register('patients', PatientViewSet, basename='patients')
urlpatterns = [
    path('', include(router.urls)),
]