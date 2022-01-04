from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import UserModel

class UserListView(APIView) :
    def get(self, request) :
        model = UserModel.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserDetailView(APIView) :
    def get(self, request, user_id) :
        model = UserModel.objects.filter(id=user_id)
        serializer = UserSerializer(UserModel)
        return Response(serializer.data)
        
    def put(self, request, user_id) :
        model = UserModel.objects.filter(id=user_id)
        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid() :
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, user_id) :
        model = UserModel.objects.filter(id=user_id)
        model.delete()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)
