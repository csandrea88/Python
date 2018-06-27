from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     
    url(r'^ninjgold/process$', views.process)
    #url(r'^ninjgold/index$', views.index)
]