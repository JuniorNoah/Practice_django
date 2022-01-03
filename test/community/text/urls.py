from django.urls import path, include
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .views import TextViewSet

urlpatterns = [
    path('text_field', TextViewSet.as_view({'get':'list'})),
]