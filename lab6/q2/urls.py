from django.urls import path
from . import views

app_name = 'q2'
urlpatterns = [
    path('index', views.index, name='index'),
    path('firstPage', views.first_page, name='first_page'),
    path('secondPage', views.second_page, name='second_page'),
]
