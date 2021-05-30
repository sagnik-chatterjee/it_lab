from django.urls import path
from .views import EmployeeForm

urlpatterns = [
    path("", EmployeeForm.as_view(), name="q2"),
]
