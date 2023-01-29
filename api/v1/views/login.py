from rest_framework import viewsets
from v1.models import User
from v1.serializers.login import LoginSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
