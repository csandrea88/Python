from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
import datetime
now = datetime.datetime.now()

def index(request):
    return render(request,'cour/index.html')

def register(request):

    reg_errors = Users.objects.register_validator(request.POST)
    # print "Are there any errors: {}".format(reg_errors)
    # print "TYPE OF THING IS {}".format(type(reg_errors))
    if type(reg_errors) == list:
        for error in reg_errors:
            messages.error(request,error)
        return redirect ("/")
    else:
        request.session['userid'] = reg_errors.id 
        return redirect ("/course")

def login(request):  #add save userid to session 
    print request.POST

    login_errors = Users.objects.login_validator(request.POST)

    if len(login_errors) > 0:
        for error in login_errors:
           messages.error(request,error)
        return redirect("/")

    login = Users.objects.filter(email = request.POST['email'])

    if len(login) == 0:
        login_errors.append("Login: Email does not exist, invalid login")
        for error in login_errors:
            messages.error(request,error)
        return redirect("/") 

    elif len(login) == 1:
        User_Password = login[0].Password
        User_id = login[0].id
        print User_id, User_Password, request.POST['password']
        if bcrypt.checkpw(request.POST['password'].encode(), User_Password.encode()) == True:
            request.session['userid'] = User_id
            print request.session['userid']
            print "TRYINNG TO REDIRECT!!!!!"
            return redirect("/course")

        else:
            login_errors.append("Login: Invalid Password")
            if login_errors > 0:
                for error in login_errors:
                    messages.error(request,error)
                return redirect("/")     

def logout(request):
    del request.session['userid'] 
    return redirect ("/") 

# Course Routes
def course(request):
    print "i am  in course"
    context = {
        "courses": Courses.objects.all()
    }
    return render(request,'cour/courses.html', context)

# def delete(request, id):  
#     context = { 
#         "course": Courses.objects.get(id=id)
#     }
#     return render(request,'cour/delete.html',content)

# def add(request):
#     print "in add"
#     return redirect("/course")

# def remove(request):
#     print "in remove "
#     #get id from hidden form field 
#     return redirect("/delete/"+id) #need syntax

def like(request, id):
    
    print "in like"
    user = Users.objects.get(id=request.session['userid'])
    print user
    course = Courses.objects.get(id=id)
    print course
    print now
    course.Likes.add(user)
    course.save()

    return redirect("/course")

# # def edit(request):
# #     print "in edit"
# #     return redirect("/")

# def destroy(request, id):
#     print "in destroy"
#     #perform delete
#     return redirect("/course")