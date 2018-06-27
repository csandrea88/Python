from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     
    url(r'^survform/process$', views.process),
    url(r'^survform/result$', views.result),
    url(r'^survform/goback$', views.goback)
]