from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     
    url(r'^amad/process$', views.process),
    url(r'^amad/checkout$', views.checkout),
    url(r'^amad/goback$', views.goback)
   
]