from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import TextModel
from .serializers import TextSerializer

class TextViewSet(viewsets.ModelViewSet) :
    queryset = TextModel.objects.all()
    Serializer_class = TextSerializer