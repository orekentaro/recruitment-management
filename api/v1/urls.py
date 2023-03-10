from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()


urlpatterns = [path("user/", views.UserViewSet.as_view(), name="user")]

urlpatterns.append(path("", include(router.urls), name="api"))
