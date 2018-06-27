from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
import datetime 
from datetime import date
from datetime import datetime


def index(request):
    return render(request,'pystack/index.html')

