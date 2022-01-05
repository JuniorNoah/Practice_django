from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.community_list),
    path('crud/<int:pk>/', views.community_datail),
]