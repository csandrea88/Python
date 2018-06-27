from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'logreg/index.html')

def success(request):
    return render(request,'logreg/success.html')


def register(request):

    reg_errors = Users.objects.register_validator(request.POST)
    print "Are there any errors: {}".format(reg_errors)
    print "TYPE OF THING IS {}".format(type(reg_errors))
    if type(reg_errors) == list:
        for error in reg_errors:
            messages.error(request,error)
        return redirect ("/")
    else:
        request.session['userid'] = reg_errors.id 
        return redirect ("/success")

def login(request):  #add save userid to session 
    
    login_errors = Users.objects.login_validator(request.POST)

    if len(login_errors) > 0:
        
        for error in login_errors:
           messages.error(request,error)
        return redirect ("/")

    login = Users.objects.filter(email = request.POST['email'])

    if len(login) == 0:
        login_errors.append("Login: Email does not exist, invalid login")
        if login_errors > 0:
            for error in login_errors:
                messages.error(request,error)
        return redirect ("/") 

    elif len(login) == 1:
        User_Password = login[0].Password
        User_id = login[0].id
        print User_id, User_Password, request.POST['password']
        if bcrypt.checkpw(request.POST['password'].encode(), User_Password.encode()) == True:
            request.session['userid'] = User_id
            print request.session['userid']
            return redirect ("/success")
        else:
            login_errors.append("Login: Invalid Password")
            if login_errors > 0:
                for error in login_errors:
                    messages.error(request,error)
                return redirect ("/")     

def logout(request):
    print request.session['userid'] 
    del request.session['userid'] 
    return redirect ("/") 