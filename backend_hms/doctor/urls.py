from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DoctorList

router = DefaultRouter()
router.register('doctors', DoctorList, basename='doctors')

urlpatterns = [
    path('', include(router.urls)),
]