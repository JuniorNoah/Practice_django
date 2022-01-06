from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.black_list),
    path('list/<int:pk>/', views.black_datail),
]