from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.urls import reverse

from block.models import Blacklist
from .serializers import BlockSerializer

class BlockListView(APIView) :
    def get(self, request) :
        model = Blacklist.objects.all()
        serializer = BlockSerializer(model, many=True)
        return Response(serializer.data, status=201)

    def post(self, request) :
        serializer = BlockSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BlockDetailView(APIView) :
    def get(self, request, block_id) :
        model = Blacklist.objects.filter(id=block_id)
        serializer = BlockSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, block_id) :
        model = Blacklist.objects.filter(id=block_id).first()
        serializer = BlockSerializer(model, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, block_id) :
        model = Blacklist.objects.filter(id=block_id)
        model.delete()
        serializer = BlockSerializer(model, many=True)
        return Response(serializer.data)