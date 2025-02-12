from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DepartmentList

router = DefaultRouter()
router.register('departments', DepartmentList, basename="departments")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]