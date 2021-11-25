from django.contrib import admin
from django.urls import path

#from webkurs.elsysapp.svar import spm1
from .views import fetch_results, get_sensor_data, index, q_page0, q_page1, q_page2 ,chart,see_results, choose_guest, fetch_questions, post_question_res #Relativ import av viewsfunksjonen

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
    path('fetch_questions', fetch_questions ,name='fetch_questions'),
    path('post_question_res', post_question_res ,name='post_question_res'),
    path('fetch_results', fetch_results ,name='fetch_results'),
    #Garbage
    path('sensor/', get_sensor_data,name='get_sensor_data'),
    path('chart/', chart,name='chart'),
]