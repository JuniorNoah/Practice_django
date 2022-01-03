from django.urls import path, include
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .views import UserViewSet

urlpatterns = [
    path('User', UserViewSet.as_view({'get':'list', 'put':'update', 'delete':'destroy', 'post':'create'})),
]