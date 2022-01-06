from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.text_list),
    path('crud/<int:pk>/', views.text_datail),
]