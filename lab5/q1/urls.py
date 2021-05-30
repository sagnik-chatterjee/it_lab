from django.conf.urls import url
from .views import TeacherFormView

urlpatterns = [
    url("", TeacherFormView.as_view(), name="q1"),
]
