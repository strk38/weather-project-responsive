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

    timezone=data['timezone']
    t_hours=timezone//3600
    t_min=(timezone%3600)//60
    #print('h ',t_hours,' m ',t_min)

    sunrise_m=data['sys']['sunrise']
    sunrise_m=str(datetime.datetime.utcfromtimestamp(sunrise_m))

    sunrise=0
    sr_h=int(sunrise_m[11:13])+t_hours
    sr_min=int(sunrise_m[14:16])+t_min
    if sr_h<10 and sr_min<10:
        sunrise='0'+str(sr_h)+':0'+str(sr_min)+':'+sunrise_m[17:]
    else:
        sunrise=str(sr_h)+':'+str(sr_min)+':'+sunrise_m[17:]
    #print(sunrise[11:])

    sunset_m=data['sys']['sunset']
    sunset_m=str(datetime.datetime.utcfromtimestamp(sunset_m))
    sunset_m=sunset_m[11:]

    sunset=0
    ss_h=int(sunset_m[:2])+t_hours
    ss_min=int(sunset_m[3:5])+t_min
    if ss_min<10:
        sunset=str(ss_h)+':0'+str(ss_min)+':'+sunset_m[6:]
    else:
        sunset=str(ss_h)+':0'+str(ss_min)+':'+sunset_m[6:]
    #print(sunset[:])
    
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
