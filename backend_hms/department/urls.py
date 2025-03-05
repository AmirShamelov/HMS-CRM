from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DepartmentList, get_my_department

router = DefaultRouter()
router.register('departments', DepartmentList, basename="departments")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('departments/get_my_department/', get_my_department, name='get_my_department' ),
    path('', include(router.urls)),
]