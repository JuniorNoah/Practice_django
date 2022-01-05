from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.head_list),
    path('crud/<int:pk>/', views.head_datail),
]