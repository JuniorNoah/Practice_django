from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.select_list),
    path('crud/<int:pk>/', views.select_datail),
]