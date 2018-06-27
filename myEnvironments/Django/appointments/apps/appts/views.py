from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
import datetime 
from datetime import date
from datetime import datetime


def index(request):
    return render(request,'appts/index.html')

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
        request.session['first_name'] = reg_errors.first_name

        return redirect ("/appts")

def login(request):  
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
        first_name = login[0].first_name

        print User_id, User_Password, request.POST['password']
        if bcrypt.checkpw(request.POST['password'].encode(), User_Password.encode()) == True:
            request.session['userid'] = User_id
            request.session['first_name'] = first_name
            return redirect("/appts")

        else:
            login_errors.append("Login: Invalid Password")
            if login_errors > 0:
                for error in login_errors:
                    messages.error(request,error)
                return redirect("/")     

def logout(request):
    del request.session['userid'] 
    del request.session['first_name'] 
    return redirect ("/") 



# appt Routes
def appts(request):
    print "i am  in appt"
    
    today_appts = Appts.objects.get(id=4)
    print "appts date field type:  ",type(today_appts.date), today_appts.date, type(date.today()),date.today()
    today_appts = Appts.objects.filter(date__exact= date.today())
    #print "length of ", len(today_appt) 
    #print "length of today_appts:", len(today_appts)
    #appt_date = datetime.strptime(todys_appts.date, '%Y-%m-%d').date() 
    #print "appts date field type afer strptime: ", type(appt_date.date)
    context = {
        #"appts": Appts.objects.all(),
        "today_appts": Appts.objects.filter(date__exact= date.today()),
        "user_appts": Appts.objects.filter(user=Users.objects.get(id=request.session['userid']))
    }
    return render(request,'appts/appts.html', context)


def add(request):
    print "in add view"

    add_errors = Appts.objects.Appts_validator(request.POST)

    appt_date = datetime.strptime(request.POST['adddate'], '%Y-%m-%d').date()
    print "appt_date and its type: ", appt_date, type(appt_date)

    #verification that appot info is not on the database
    
    if len(add_errors) == 0: 
        newappt = Appts.objects.create(
            task=request.POST['addtask'], 
            #date=request.POST['adddate'],
            date=appt_date,
            time=request.POST['addtime'],
            status = "Pending",
            user = Users.objects.get(id=request.session['userid'])
        )
    
    if len(add_errors) > 0:
        for error in add_errors:
            messages.error(request,error)

    print "about to redirect to appt"   
    return redirect("/appts")

# def like(request, id):
    
#     print "in like"
#     user = Users.objects.get(id=request.session['userid'])
#     print user
#     course = Courses.objects.get(id=id)
#     print course
#     print now
#     course.Likes.add(user)
#     course.save()

#     return redirect("/course")

def edit(request, id):
    print "in edit"
    context = {
        "upt_appt": Appts.objects.get(id = id)
    }
   
    return render(request,'appts/update.html', context)
   

def update(request, id):
    print "in update"

    errors = Appts.objects.update_validator(request.POST)
    
    print "returned from update"

    if len(errors) > 0:
        for error in errors:
            messages.error(request,error)
            
        return redirect("/" + id + "/edit")
    
    else:
        update_rec = Appts.objects.get(id = id)
        appt_date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()

        if update_rec:
            update_rec.task = request.POST['task']
            update_rec.status = request.POST['status']
            #update_rec.date = request.POST['date']
            update_rec.date = appt_date
            update_rec.time = request.POST['time']
            update_rec.save()
            return redirect("/appts")
        
        else: 
            messages.error(request,"Cannot update, record is missing")
            update_rec = Appts.objects.get(id = id)

def delete(request, id):

    delete_rec = Appts.objects.get(id = id)
    print "delete_rec:", delete_rec 
    delete_rec.delete()

    return redirect("/appts")

