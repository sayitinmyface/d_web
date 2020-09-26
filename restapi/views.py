from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import include, path

# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=22b142ec10552ddfa0aa658e9121f46e'

    if request.method == 'post':
        form = CityForm(request.post)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in citeies:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon'        : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather' : weather_data, 'form' : form}

    return render(request, 'weather/weather.html', context)
