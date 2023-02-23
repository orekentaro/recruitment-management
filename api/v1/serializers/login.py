from rest_framework import serializers

from v1.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("mail", "password")
