from django.urls import path, include
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .views import MainViewSet

urlpatterns = [
    path('main', MainViewSet.as_view({'get':'list'})),
]