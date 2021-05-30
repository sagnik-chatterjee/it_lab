from django.urls import path
from .views import BasicArithmatic

urlpatterns = [
    path("", BasicArithmatic.as_view(), name="q3"),
]
