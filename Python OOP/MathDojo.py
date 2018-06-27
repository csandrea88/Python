class MathDojo(object):
    def __init__(self):
        self.num = 0

    def add(self,*arrays):
    
        for i in range(len(arrays)):  
            if isinstance(arrays[i], list):     
                for arr_anum1 in arrays[i]:
                    self.num += arr_anum1 
            else:
               self.num += arrays[i] 

        return self

    def subtract(self,*arrays):

        for i in range(len(arrays)):  
            if isinstance(arrays[i], list):     
                for arr_anum1 in arrays[i]:
                    self.num -= arr_anum1 
            else:
               self.num -= arrays[i] 

        return self

    def result(self):
        print "Results: {}".format(self.num)
        return self

md= MathDojo().add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
#md= MathDojo().add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
#md= MathDojo().add(2).add(2,5).subtract(3,2).result()
#my_Animal = Animal("Cat",9).walk().walk().walk().run().run().display_health()
#my_dog = Dogs("Duncan",150).walk().walk().walk().run().run().pet().display_health()



