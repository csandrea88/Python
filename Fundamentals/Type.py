
#list = ['magical unicorns',19,'hello',98.98,'world']
list = [2,3,1,7,4,12.2]
#list = ['magical','unicorns']

strmsg = ""
Sum = 0.0

for i in list:
    
    if isinstance(i, int):
        Sum += i 
        
    elif isinstance(i, str):
        #strmsg += " "
        strmsg += " " + i + ","

if Sum > 0 and strmsg != "":
    print("this list is of mixed types") 
    print("String: {}".format(strmsg))
    print("Sum: {}".format(Sum))

elif Sum > 0 and strmsg == "":
    print("this list is only integers") 
    print("Sum: {}".format(Sum))

elif strmsg != "" and Sum == 0:
    print("this list is only strings") 
    print("String: {}".format(strmsg))


