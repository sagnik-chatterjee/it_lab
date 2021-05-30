from django import forms
from django.forms import widgets
from django.forms.fields import CharField, EmailField, IntegerField


class BasicForm(forms.Form): 
    username = CharField(required=True)
    password = CharField(widget=widgets.PasswordInput(), required=False)
    email = CharField(widget=widgets.EmailInput(), required=False)
    contact= IntegerField(min_value=1000000000,max_value=9999999999,required=False)

