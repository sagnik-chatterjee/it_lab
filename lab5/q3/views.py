from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BasicArithmatic(TemplateView):
    template_name = "q3.html"
