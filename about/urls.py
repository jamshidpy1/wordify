from django.urls import path
from .views import FeedbackListCreateAPIView, FeedbackRUDAPIView


urlpatterns = [
    path('list-create/', FeedbackListCreateAPIView.as_view()),
    path('rud/<int:pk>/', FeedbackRUDAPIView.as_view()),
]