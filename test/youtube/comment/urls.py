from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.comment_list),
    path('crud/<int:pk>/', views.comment_datail),
]