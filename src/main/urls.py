from django.urls import path
from .views import main,services_page



urlpatterns = [
    path('', main, name='main'),  
    path('services/', services_page, name='services'),
    path('post-ads/', main, name='post-ads'),

]