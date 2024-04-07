from django.shortcuts import render

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(letter, symbol, number):
    password_list = []

    for _ in range(letter):
        password_list.append(random.choice(letters))

    for _ in range(symbol):
        password_list.append(random.choice(symbols))

    for _ in range(number):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    return ''.join(password_list)


def password_manager(request):
    password = None

    if request.method == 'POST':
        letter = int(request.POST.get('letters'))
        symbol = int(request.POST.get('symbols'))
        number = int(request.POST.get('numbers'))

        password = generate_password(letter, symbol, number)

    return render(request, 'password_form.html', {'password': password})


def password_show(request):
    password = request.GET.get('password', None)
    return render(request, 'password.html', {'password': password})
