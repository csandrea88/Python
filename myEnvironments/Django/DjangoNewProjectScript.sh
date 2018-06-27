#!/bin/bash
django-admin startproject PythonStackProj
cd PythonStackProj
mkdir apps
cd apps
touch __init__.py
../manage.py startapp pystack
python manage.py makemigrations
python manage.py migrate
cd apps
cd pystack
mkdir templates
mkdir static
cd static 
mkdir css
mkdir js
mkdir images
cd css
mkdir pystack
cd pystack
touch pystack.css



