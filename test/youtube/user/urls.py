from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.user_list),
    path('crud/<int:pk>/', views.user_datail),
]