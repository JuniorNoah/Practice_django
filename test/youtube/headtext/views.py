from rest_framework.viewsets import ModelViewSet
from .models import HeadTextModel
from .serializers import HeadtextSerializer

class HeadTextViewSet(ModelViewSet) :
    queryset = HeadTextModel.objects.all()
    serializer_class = HeadtextSerializer
    
head_list = HeadTextViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

head_datail = HeadTextViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})