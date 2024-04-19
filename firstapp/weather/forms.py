from django.forms import ModelForm
from .models import weather


class CityForm(ModelForm):
    class Meta:
        model = weather
        fields = '__all__'
