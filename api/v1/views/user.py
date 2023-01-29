from rest_framework import generics
from v1.models import User
from v1.serializers import UserSerializer

from rest_framework.views import Response


class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        super().create(serializer.validate_data)
        return Response("OK")
