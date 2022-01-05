from rest_framework.viewsets import ModelViewSet
from .models import TextModel
from .serializers import TextSerializer

class TextViewSet(ModelViewSet) :
    queryset = TextModel.objects.all()
    serializer_class = TextSerializer
    
text_list = TextViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

text_datail = TextViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})