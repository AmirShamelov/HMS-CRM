from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'phone', 'address', 'birth_date', 'blood', 'allergies', 'chronic_disease']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
