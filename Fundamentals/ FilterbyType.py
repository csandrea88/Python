#x = 45
#x = 100
#x = 455
#x = 0
#x = -23
#x = "Rubber baby buggy bumpers"
#x = "Experience is simply the name we give our mistakes"
#x = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
#x = ""
#x = [1,7,4,21]
#x = [3,5,7,34,3,2,113,65,8,89]
#x = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
#x = []
x = ['name','address','phone number','social security number']

if isinstance(x, int):
    if x>=100:
        print("That's a big number")
    else: 
        print("That's a small number")

elif isinstance(x, str):
    if len(x)>50:
        print("Long Sentence")
    else: 
        print("Short Sentence")

elif isinstance(x,list):
    if len(x)>10:
        print("Long list")
    else: 
        print("Short list")