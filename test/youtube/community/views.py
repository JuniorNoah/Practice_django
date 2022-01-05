from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CommSerializer
from .models import CommunityModel

class CommListView(APIView) :
    def get(self, request) :
        model = CommunityModel.objects.all()
        serializer = CommSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = CommSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CommDetailView(APIView) :
    def get(self, request, comm_id) :
        model = CommunityModel.objects.filter(id=comm_id)
        serializer = CommSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, comm_id) :
        model = CommunityModel.objects.filter(id=comm_id).first()
        serializer = CommSerializer(model, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, comm_id) :
        model = CommunityModel.objects.filter(id=comm_id)
        model.delete()
        serializer = CommSerializer(model, many=True)
        return Response(serializer.data)
