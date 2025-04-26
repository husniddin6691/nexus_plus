from django.urls import path
from .views import BlogGenericAPIView, BlogGenericDetailAPIView


urlpatterns = [
    path('', BlogGenericAPIView.as_view(), name='blog-list'),
    path('<int:pk>/', BlogGenericDetailAPIView.as_view(), name='blog-detail')
]
