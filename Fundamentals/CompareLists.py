
# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','milk']

list_one = [1,2,5,6,5,16]
list_two = ['1','2','5','6','5','16']

print(cmp(list_one,list_two))

lcomp = cmp(list_one,list_two)

if lcomp == -1 or lcomp == 1:
    print("Lists are not same")
elif lcomp == 0:
    print("Lists are same")



