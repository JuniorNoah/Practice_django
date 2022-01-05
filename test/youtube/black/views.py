from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlackSerializer
from .models import BlackList

class BlackListView(APIView) :
    def get(self, request) :
        model = BlackList.objects.all()
        serializer = BlackSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = BlackSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BlackDetailView(APIView) :
    def get(self, request, user_id) :
        model = BlackList.objects.filter(id=user_id)
        serializer = BlackSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, user_id) :
        model = BlackList.objects.filter(id=user_id).first()
        serializer = BlackSerializer(model, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, user_id) :
        model = BlackList.objects.filter(id=user_id)
        model.delete()
        serializer = BlackSerializer(model, many=True)
        return Response(serializer.data)
