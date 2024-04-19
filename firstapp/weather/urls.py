from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_weather_view, name='weather'),
    # path('weather-info/', views.weather_info_view, name='weather_info'),
]
