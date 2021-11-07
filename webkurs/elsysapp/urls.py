from django.contrib import admin
from django.urls import path

#from webkurs.elsysapp.svar import spm1
from .views import get_sensor_data, index, q_page0, q_page1, q_page2 ,chart,see_results, choose_guest, get_question, return_question_score #Relativ import av viewsfunksjonen

appname = "elsysapp"
urlpatterns = [
    #pages
    path('', index, name='index'),
    path('q_page0', q_page0, name='q_page0'),
    path('q_page1', q_page1, name='q_page1'),
    path('q_page2', q_page2, name='q_page2'),
    path('see_results', see_results, name='see_results'),
    path('choose_guest', choose_guest, name='choose_guest'),
    #data
    path('get_question', get_question ,name='get_question'),
    path('return_question_score', return_question_score ,name='return_question_score'),
    #Garbage
    path('sensor/', get_sensor_data,name='get_sensor_data'),
    path('chart/', chart,name='chart'),
]