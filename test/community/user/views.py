from django.core.exceptions import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserSerializer 

class UserViewSet(viewsets.ModelViewSet) :
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self) :
        return UserModel.objects.all()
    
    def user_list(self, request) :
        if request.method == 'GET' :
            serializer = UserSerializer(many=True)
            return Response(serializer)
        elif request.mothod == 'POST' :
            serializer = UserSerializer(self.get_queryset(), many=True)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)            
        