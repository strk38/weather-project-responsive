from django.shortcuts import render, HttpResponse
import datetime
import requests
# Create your views here.
def home(request):

    if 'city' in request.POST:
        city =request.POST['city']
    else:
        city='Chittagong'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a79c348ffad680ebc3516e408d438af0'
    PARAMS={'units':'metric'}

    data=requests.get(url,PARAMS).json()
    print(city,': ',data)

    icon=data['weather'][0]['icon']
    temp=data['main']['temp']
    day=datetime.date.today()
    description=data['weather'][0]['main']
    country=data['sys']['country']
    location=city+', '+country

    longitude=data['coord']['lon']
    latitude=data['coord']['lat']

    wind_speed=data['wind']['speed']
    feels_like=data['main']['feels_like']

    sunrise=data['sys']['sunrise']
    sunset=data['sys']['sunset']

    humidity=data['main']['humidity']
    temp_max=data['main']['temp_max']
    temp_min=data['main']['temp_min']
    
    context={
        'icon':icon, 'temp':temp, 'day':day, 'description':description, 'city':location,
        'longitude':longitude, 'latitude':latitude, 
        'wind_speed':wind_speed, 'feels_like':feels_like,'sunrise':sunrise,  'sunset':sunset, 
        'humidity':humidity, 'temp_max':temp_max, 'temp_min':temp_min
    }

    return render(request,'index.html',context)
