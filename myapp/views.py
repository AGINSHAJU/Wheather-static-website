from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseBadRequest  # Import HttpResponseBadRequest
from .models import Contact
from geopy.geocoders import Nominatim
import requests
from datetime import datetime
import json

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('number')

        if not name or not email or not mobilenumber:
            messages.error(request, "All fields are required.")
            return redirect('home')

        try:
            Contact.objects.create(name=name, email=email, mobilenumber=mobilenumber)
            messages.success(request, "Your contact information has been submitted successfully.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('index')


    return render(request, 'index.html')

def whether(request):
    data = {}
    
    if request.method == 'POST':
        city = request.POST.get('city')
        
        if not city:
            return HttpResponseBadRequest("City parameter is missing")
        
        try:  
            # OpenWeatherMap API request
            response = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=cdf7755e6d6408ebf3ffca0f6bda2033'
            )
            
            list_of_data = response.json()
            
            # Check if the city is found
            if list_of_data.get('cod') != 200:
                raise ValueError("City not found")
            
            data = {
                "city_name": str(list_of_data['name']),
                "country_code": str(list_of_data['sys']['country']),
                "longitude": float(list_of_data['coord']['lon']),
                "latitude": float(list_of_data['coord']['lat']),
                "temp": f"{list_of_data['main']['temp']} °C",
                "feels_like": f"{list_of_data['main']['feels_like']} °C",
                "temp_min": f"{list_of_data['main']['temp_min']} °C",
                "temp_max": f"{list_of_data['main']['temp_max']} °C",
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
                "speed": str(list_of_data['wind']['speed']),
                "deg": str(list_of_data['wind']['deg']),
                "gust": str(list_of_data['wind'].get('gust', 'N/A')),
                "rain": str(list_of_data.get('rain', {}).get('1h', 'N/A')),
                "visibility": str(list_of_data.get('visibility', 'N/A')),
                "clouds": str(list_of_data.get('clouds', {}).get('all', 'N/A')),
                "sunrise": datetime.utcfromtimestamp(list_of_data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
                "sunset": datetime.utcfromtimestamp(list_of_data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
            }
        
        except requests.RequestException as e:
            return HttpResponseBadRequest(f"Error fetching weather data: {e}")
        
        except ValueError as e:
            return HttpResponseBadRequest(str(e))
    
    return render(request, 'whether.html', data)

def whether_view(request):
    # Simulate server processing time
    import time
    time.sleep(1)  # 1 second delay

    # Your existing view logic here
    context = {
        # Example context data
        'country_code': 'Example Country Code',
        'coordinate': 'Example Coordinate',
        'temp': 'Example Temp',
        'pressure': 'Example Pressure',
        'humidity': 'Example Humidity',
        # ... other context variables ...
    }
    return render(request, 'whether.html', context)  
  
def about(request):  # Note: the function name is about_us, not about
    context = {
        'app_name': 'Weather-Finding Website'
    }
    return render(request, 'about.html', context)
