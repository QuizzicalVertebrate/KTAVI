from django.urls import path
from .views import fake_api, fake_api2,  base, input, test




urlpatterns = [
    path('', base, name = 'base'),
    path('order', input, name = 'order_create'),
    path('secondaries/', fake_api, name = 'secondaries'),
    path('tertiaries/', fake_api2, name = 'tertiaries'),
    path('test/', test, name = 'test'),
 
]
