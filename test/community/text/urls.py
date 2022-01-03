from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('TextModel', views.TextViewSet)

urlpatterns = [
    path('', include(router.urls))
]
