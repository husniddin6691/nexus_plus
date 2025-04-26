from django.urls import path, include

urlpatterns = [
    path('category/', include('api.category.urls'), name='category'),
    path('brand/', include('api.brand.urls'), name='brand'),
    path('region/', include('api.region.urls'), name='region'),
    path('product/', include('api.product.urls'), name='product'),
    path('blog/', include('api.blog.urls'), name='blog'),
]