from django.db import models
from django.db.models.base import Model

# Create your models here.
class SensorData(models.Model):#definerer klassen
  data = models.CharField(max_length=128)#lager et 128 char tekstfelt 
  sensor_id = models.IntegerField() #lager et heltallsfelt
  timestamp = models.DateField(auto_now_add=True) #lager et datofelt

  def __str__(self):
    return f'Data: {self.data}, Sensor ID: {self.sensor_id}, timestamp: {self.timestamp}'
    '''print(SensorData.data)
    print(SensorData.sensor_id)
    print(SensorData.timestamp)'''
