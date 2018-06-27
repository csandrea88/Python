from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),   
    url(r'^index$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^appts$', views.appts),
    url(r'^add$', views.add),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/update$', views.update),
    url(r'^update/dashboard', views.appts),
    url(r'^(?P<id>\d+)/delete$', views.delete)
    
    #url(r'^success$', views.success), #not using anymore 
    #url(r'^edit$', views.edit), doing this last 
    #url(r'^remove$', views.remove),
    #url(r'^like$', views.like),
    #url(r'^destroy/(?P<number>[0-9]+)$', views.destroy), 
]