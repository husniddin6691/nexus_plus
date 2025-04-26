from django.urls import path
from .views import CategoryView,CategoryDetailView,CategoryListView

# serializers


urlpatterns = [
    path('', CategoryView.as_view(), name='category_view'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('list/', CategoryListView.as_view(), name='category_list'),

]

