

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }




print "Students:"

for i in range(len(users["Students"])):
    name_length = len(users["Students"][i]["first_name"]) + len(users["Students"][i]["last_name"])
    print "{} - {} {} - {}".format(i, users["Students"][i]["first_name"], users["Students"][i]["last_name"], name_length)

print "Instructors:"

for i in range(len(users["Instructors"])):    
    name_length = len(users["Instructors"][i]["first_name"]) + len(users["Instructors"][i]["last_name"])
    print "{} - {} {} - {}".format(i, users["Instructors"][i]["first_name"], users["Instructors"][i]["last_name"], name_length)

