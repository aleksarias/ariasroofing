from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )

class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = CustomerProfile