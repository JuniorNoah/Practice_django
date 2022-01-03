from rest_framework import viewsets
from .models import TextModel
from .serializers import TextSerializer

class TextViewSet(viewsets.ModelViewSet) :
    queryset = TextModel.objects.all()
    serializer_class = TextSerializer
    
    def get_queryset(self) :
        return TextModel.objects.all()