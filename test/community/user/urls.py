from django.urls import path, include
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .views import UserViewSet

urlpatterns = [
    path('user_info', UserViewSet.as_view({'get':'list'})),
]