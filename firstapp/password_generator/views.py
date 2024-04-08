from django.shortcuts import render, redirect
from .forms import PasswordGeneratorForm
from .models import GeneratedPassword
from .utils import generate_password
from django.contrib.auth.hashers import make_password


def home(request):
    return render(request, 'home.html')


def password_generator_form(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            website_name = form.cleaned_data['website_name']
            total_length = form.cleaned_data['total_length']
            numbers = form.cleaned_data['numbers']
            symbols = form.cleaned_data['symbols']
            password = generate_password(numbers, symbols, total_length)
            hashed_password = make_password(password)
            generated_password = GeneratedPassword.objects.create(website_name=website_name, password=password)
            generated_password.save()
            return redirect('password_list')
    else:
        form = PasswordGeneratorForm()
    return render(request, 'password_generator_form.html', {'form': form})


def password_list(request):
    generated_passwords = GeneratedPassword.objects.all()
    return render(request, 'password_list.html', {'generated_passwords': generated_passwords})
