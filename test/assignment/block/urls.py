from django.urls import path
from .views import BlockListView, BlockDetailView

urlpatterns = [
    path('list/', BlockListView.as_view()),
    path('list/<int:block_id>', BlockDetailView.as_view()),
]
