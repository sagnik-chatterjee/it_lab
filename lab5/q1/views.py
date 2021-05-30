from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class TeacherFormView(TemplateView):
    template_name = "q1.html"
