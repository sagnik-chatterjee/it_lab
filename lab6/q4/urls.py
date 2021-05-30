from django.urls import path
from . import views

app_name = 'q4'
urlpatterns = [
    path('', views.index, name='index'),
    path('produce_bill', views.produce_bill, name='produce_bill'),
]
