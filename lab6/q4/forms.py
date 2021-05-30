from django import forms
from django.forms import widgets
from django.forms.fields import CharField, EmailField, IntegerField

companies = [
    ('HP', 'HP'),
    ('Nokia', 'Nokia'),
    ('Samsung', 'Samsung'),
    ('Motorolla', 'Motorolla'),
    ('Apple', 'Apple'),
]

class BasicForm(forms.Form):
    company = forms.ChoiceField(widget=forms.RadioSelect, choices=companies)
    mobile = forms.BooleanField(required=False)
    laptop = forms.BooleanField(required=False)
    quantity = forms.IntegerField()

