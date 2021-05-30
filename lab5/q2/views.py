from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class EmployeeForm(TemplateView):
    template_name = "q2.html"
