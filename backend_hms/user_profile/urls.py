from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register('my_profile', UserViewSet, basename='my_profile')
router.register('user', ProfileViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]