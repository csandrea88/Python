

# def odd_even():

    # for x in range(2000):
       
    #     if x % 2 == 0:    
    #         print "Number is {}, This is an even number".format(x)
    #     else: 
    #         print "Number is {}, This is an odd number".format(x)

# odd_even()

def multiply(list,Multiplier):

    
    for i in range(len(list)):
    
        list[i] *= Multiplier
       

    return list

outlist = multiply([2, 4, 10, 16],5)
print(outlist)