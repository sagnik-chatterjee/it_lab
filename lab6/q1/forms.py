from django import forms
from django.forms import widgets

car_manufacturers = [
    ('Q2', 'Audi'),
    ('Aspire', 'Ford'),
    ('SL400', 'Mercedes'),
    ('F8', 'Ferrari'),
    ('Model S','Tesla'),
    ('Cerna', 'Toyota')
]

class BasicForm(forms.Form):
    car_manufacturer = forms.CharField(label='Select car manufacturer.', widget=forms.Select(choices=car_manufacturers))
    model_name = forms.CharField()
