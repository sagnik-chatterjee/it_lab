from django.db import models

# Create your models here.

## here we create the db models for our data 
from django import forms 

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()  
    class Meta:
        ordering=('timestamp',)
    
class BlogPostForm(forms.ModelForm):
    class Meta:
        model =BlogPost 
        exclude=('timestamp',)

