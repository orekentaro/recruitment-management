from django.db import transaction
from rest_framework import generics
from rest_framework.views import Response

from v1.models import User
from v1.serializers import CreateUserSerializer


class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    @transaction.atomic
    def create(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("OK")
