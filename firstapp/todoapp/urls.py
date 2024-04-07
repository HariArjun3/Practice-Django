from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_manager, name='generate_password'),
    path('password/', views.password_show, name='show_password'),
]
