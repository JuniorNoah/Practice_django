from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HeadtextSerializer
from .models import HeadTextModel

class HeadListView(APIView) :
    def get(self, request) :
        model = HeadTextModel.objects.all()
        serializer = HeadtextSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = HeadtextSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class HeadDetailView(APIView) :
    def get(self, request, head_id) :
        model = HeadTextModel.objects.filter(id=head_id)
        serializer = HeadtextSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, head_id) :
        model = HeadTextModel.objects.filter(id=head_id)
        serializer = HeadtextSerializer(model, data=request.data)
        if serializer.is_valid() :
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, head_id) :
        model = HeadTextModel.objects.filter(id=head_id)
        model.delete()
        serializer = HeadtextSerializer(model, many=True)
        return Response(serializer.data)
