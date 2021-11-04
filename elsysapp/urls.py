from django.contrib import admin
from django.urls import path
from .views import get_sensor_data, index, q_page0, q_page1, q_page2 ,chart,see_results, choose_guest #Relativ import av viewsfunksjonen

appname = "elsysapp"
urlpatterns = [
    path('', index, name='index'),
    path('q_page0', q_page0, name='q_page0'),
    path('q_page1', q_page1, name='q_page1'),
    path('q_page2', q_page2, name='q_page2'),
    path('see_results', see_results, name='see_results'),
    path('choose_guest', choose_guest, name='choose_guest'),
    
    #Garbage
    path('sensor/', get_sensor_data,name='get_sensor_data'),
    path('chart/', chart,name='chart'),
]