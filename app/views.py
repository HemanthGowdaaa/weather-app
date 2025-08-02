from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    api_key = "ddbaede094def9749bc5f27a9555b431"
    city = request.GET.get('city',"bangalore")
    api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    api = requests.get(api_url).json()
    temp = api['main']['temp']
    countory = api['name']
    cty = api['sys']["country"]
    ctx = {"temp1":temp,
           "city":countory,
           "country":cty}
    return render(request,"index.html",ctx)