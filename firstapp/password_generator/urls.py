# password_generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.password_generator_form, name='password_generator_form'),
    path('list/', views.password_list, name='password_list'),
]
