from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),   
    url(r'^index$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^course$', views.course),
    #url(r'^add$', views.add),
    #url(r'^remove$', views.remove),
    #url(r'^like$', views.like),
    url(r'^(?P<id>\d+)/like$', views.like),
    #url(r'^destroy/(?P<number>[0-9]+)$', views.destroy), 
    #url(r'^delete/(?P<number>[0-9]+)$', views.delete)
    
    #url(r'^success$', views.success), #not using anymore 
    #url(r'^edit$', views.edit), doing this last 
]