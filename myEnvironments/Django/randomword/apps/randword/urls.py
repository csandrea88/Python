from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!\
    url(r'^randword/generate$', views.generate),
    url(r'^randword/reset$', views.reset)
  ]