from django.http import HttpResponse, QueryDict,JsonResponse
from django.shortcuts import render
from .models import SensorData
from django.middleware import csrf
from elsysapp.svar import spm, edit_score

# Create your views here.
def index(request):
   print("Dette blir printa i terminalen")
   context = {}
   all_sensor_data = SensorData.objects.all() #Henter ut all sensordata fra databasen. 
   context['all_sensor_data'] = all_sensor_data #Legger sensordata til som en variabel som kan brukes i Template. 
   return render(request, "elsysapp/index.html", context)    

def choose_guest(request):
    context = {} # Tom dictionary som blir brukt senere!
    return render(request, "elsysapp/choose_guest.html", context)

def q_page0(request):
    context = {} # Tom dictionary som blir brukt senere!
    return render(request, "elsysapp/q_page0.html", context)
def q_page1(request):
    context = {} # Tom dictionary som blir brukt senere!
    return render(request, "elsysapp/q_page1.html", context)
def q_page2(request):
    context = {} # Tom dictionary som blir brukt senere!
    return render(request, "elsysapp/q_page2.html", context)

def get_question(request):
   # request should be ajax and method should be GET.
  if request.method == "GET" :
      data = spm("guest1")
      return JsonResponse(data={
      'data': data,
      'status':"Success",
      }, status = 200)
  else:
    return JsonResponse({}, status = 400)

def return_question_score(request):
  edit_score("guest1","Hvor er du fra?","Test 1")
  '''
  print("aktivert\n"+ "-"*20+"\n")
  if request.method == "POST" :
      data = str(spm("guest1"))
      return JsonResponse(data={
      'data': data,
      'status':"Success",
      }, status = 200)
  else:
    return JsonResponse({}, status = 400)
  '''


def see_results(request):
    #print("Dette blir printa i terminalen")
    context = {} # Tom dictionary som blir brukt senere!
    return render(request, "elsysapp/see_results.html", context)

def get_sensor_data(request):
    if request.method == "POST": 
        data =  QueryDict(request.body) # Gjør data fra request om til en dictionary
        sensor_id = data['sensorID'] # Lagrer sensorIDen til requesten 
        sensor_value = data['sensorData'] # Lagrer sensorverdien til requesten
    
        #Skriv koden for å lage og lagre et sensorobjekt her. 
        newSensorData = SensorData(data=sensor_value ,sensor_id=sensor_id)
        newSensorData.save()
        print(newSensorData)
        return HttpResponse("SUCCESS")
    elif request.method == "GET":
        """Dette MÅ være med! Sikkerhetsgreier."""
        csrf.get_token(request)
        return HttpResponse("")

def chart(request):

  labels = [] # Holder navnene på stolpene i stolpediagrammet.
  data = []   # Holder høyden til stolpene i diagrammet.

  objects = SensorData.objects    # Queryset som holder alle databaseobjektene.
  
  ids = set()   # Et set er en liste som ikke kan inneholde duplikater.
  [ids.add(id[0]) for id in objects.values_list("sensor_id")] # List comprehension. Hent ut alle sensor_id fra databasen og legg dem til i ids.
  ids = list(ids) # Gjør tilbake til liste for enkelhets skyld.

  counts = [0] * len(ids) # Liste som skal holde antall objekter pr. sensor_id
  for i, id in enumerate(ids):
      counts[i] = counts[i] + objects.filter(sensor_id=id).count()

  labels = ["Sensor {}".format(id) for id in ids]# Lagre alle sensor_id med 'Sensor ' foran.
  data = counts
  
  return JsonResponse(data={
      'labels': labels,
      'data': data,
  })




