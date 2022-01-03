from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet) :
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer