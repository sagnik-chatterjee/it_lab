from django import forms
from django.forms import widgets
from django.forms.fields import CharField, IntegerField

subjects = [
    ('Math', 'Math'),
    ('Phycics', 'Physics'),
    ('English', 'English'),
    ('Chemistry', 'Chemistry'),
    ('Web Dev','Web Dev'),
    ('Algorithms','Algorithms'),
]

class BasicForm(forms.Form):
    name = CharField()
    roll = IntegerField()
    subject = CharField(label='Select subject.', widget=forms.Select(choices=subjects))

    
