#Use this code to make sure your project is setup correctly
#
# from django.shortcuts import render, HttpResponse, redirect
#  # the index function is called when root is visited
# def index(request):
#   response = "Hello, I am your first request!"
#   return HttpResponse(response)

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }

  return render(request,'timedisplay/index.html', context)
