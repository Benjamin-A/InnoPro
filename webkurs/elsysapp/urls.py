from django.contrib import admin
from django.urls import path
from .views import get_sensor_data, index,start_side,chart #Relativ import av viewsfunksjonen

appname = "elsysapp"
urlpatterns = [
    path('', index, name='index'),
    path('start_side', start_side, name='start_side'),
    path('sensor/', get_sensor_data,name='get_sensor_data'),
    path('chart/', chart,name='chart'),
]