
#Multiples, Sum, Average

#Multiples
#print every odd number from 2-1,000 
for x in range(1000):
    # Check if x is !even
    if x % 2 != 0:    
        print(x)

#print every number from 5-1,000,000 that is divisible by 5
for x in range(5,1000000):
    if x % 5 == 0:    
        print(x)

#Sum & Average of list
sum = 0;

list = [1, 2, 5, 10, 255, 3]

for i in range(len(list)):
    sum += list[i]
    
print (sum, sum/len(list))   


