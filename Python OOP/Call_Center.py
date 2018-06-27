class Call(object):
    def __init__(self, id, name, phone, time, reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
        
        
    def Display_call(self):
        print "Caller id: {} name: {}, phone: {}, time: {}, reason: {}".format(self.id, self.name,self.phone, self.time, self.reason)
        return self
    
    
    
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
         
    def add_call(self, Id, name, phone, time, reason):
    # adds a new call to the end of the call list
        
        Call(Id, name, phone, time, reason)
        self.calls.append("name: {}, phone: {}".format(name,phone))
        return self

    def remove(self):
    #removes the call from the beginning of the list (index 0)
        self.calls.pop(0)
        return self

    def info(self):
    #display each call in queue and total calls in queue
        for i in range(len(self.calls)):
           print "queued call: {}".format(self.calls[i])
        print "Total in queue: {}".format(len(self.calls))
        return self

        
#now create an instance of the class
CallCenter = CallCenter().add_call(23, "andrea", "847-111-1111", "9:00AM", "Billing" )
CallCenter.add_call(23, "sue", "847-111-1111", "9:00AM", "Billing" ).info()
CallCenter.add_call(33, "andrea", "847-111-1111", "10:00AM", "Billing" ).info()
CallCenter.add_call(43, "don", "847-111-1111", "11:00AM", "Billing" ).remove().info()



