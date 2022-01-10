from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.urls import reverse
from .serializers import UserSerializer, LoginSerializer
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
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, user_id) :
        model = UserModel.objects.filter(id=user_id).first()
        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, user_id) :
        model = UserModel.objects.filter(id=user_id)
        model.delete()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)
    
class Loginview(APIView) :
    def get(self, request) :
        return Response('Input your id / pw')
    
    def post(self, request) :
        id = request.data['login_id']
        pw = request.data['login_pw']
        data_id = UserModel.objects.filter(login_id=id)
        
        # login
        if data_id.exists() :
            data_pw = UserModel.objects.filter(login_pw=pw)
            if data_pw.exists() :
                model = UserModel.objects.get(login_id=id)
                serializer = LoginSerializer(model, data=request.data)
                if serializer.is_valid() :
                    model['connection'] = True
                    return Response(serializer.data, status=201)

        return redirect(reverse('login'))            