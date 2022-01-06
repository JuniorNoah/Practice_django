from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from .models import LoginModel
from user.models import UserModel

class LoginListView(APIView) :
    def get(self, request) :
        model = LoginModel.objects.all()
        serializer = LoginSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        
        model = UserModel.objects.filter()
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)