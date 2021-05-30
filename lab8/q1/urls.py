from django.conf.urls import include ,url
from django.urls.resolvers import URLPattern 
from . import views 
from django.urls import path 

urlpatterns=[
   path('page1/',views.page1),
   path('page2/',views.page2),
]

