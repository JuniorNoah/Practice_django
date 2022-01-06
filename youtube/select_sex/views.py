from rest_framework.viewsets import ModelViewSet
from .models import SelectSexModel
from .serializers import SelectSexSerializer

class SelectSexViewSet(ModelViewSet) :
    queryset = SelectSexModel.objects.all()
    serializer_class = SelectSexSerializer
    
select_list = SelectSexViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

select_datail = SelectSexViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})