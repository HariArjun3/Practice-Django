from django.shortcuts import render, redirect
from .models import weather, SearchHistory
from .forms import CityForm
from .utils import get_weather

# Create your views here.

weather_data = []


def get_weather_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weather_info')
    else:
        form = CityForm()

    cities = weather.objects.all()
    for city in cities:
        weather_info = get_weather(city.city)
        weather_info['city'] = city.city
        weather_data.append(weather_info)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather.html', context)


def weather_info_view(request):
    generated_weather_data = weather.objects.all()
    return render(request, 'weather_info.html', {'generated_weather_data': generated_weather_data, 'weather_data': weather_data})


def clear_history(request):
    if request.method == 'POST':
        if request.user.is_authenticated:  # Check if user is authenticated
            user = request.user
            SearchHistory.objects.filter(user=user).delete()
            return redirect('/weather/')  # Redirect to weather page after clearing
        else:
            # Handle case where user is not logged in (optional: display message)
            return redirect('/weather/')  # Or redirect to login page
    else:
        return redirect('/weather/')  # Handle non-POST requests (optional)

