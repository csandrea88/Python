
#Common Python List manipulations
#.find and & .replace
words = "It's thanksgiving day. It's my birthday,too!"
print(words.find("day"))
print(words.replace("day", "month",1))

#.min & .max
x = [2,54,-2,7,12,98]
print(min(x))
print(max(x))

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print(x[:1],x[-1])

# create new list, plus insert & remove list items
x = [19,2,54,-2,7,12,98,32,10,-3,6]
newx = []
pos = (len(x)-1) / 2
x.sort()
newx = x[:pos]
del x[:pos]
x.insert(0,newx)
print(x)