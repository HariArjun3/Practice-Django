# password_generator/forms.py
from django import forms


class PasswordGeneratorForm(forms.Form):
    website_name = forms.CharField(max_length=255)
    total_length = forms.IntegerField(label='Total Length')
    numbers = forms.IntegerField(label='How many of Numbers')
    symbols = forms.IntegerField(label='How many of Symbols')

