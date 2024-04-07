from django.shortcuts import render


# Create your views here.

def home(request):
    return '<h1>Welcome</h1>'


def wish(request):
    return render(request, 'home.html')
