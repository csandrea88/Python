class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "bike's price: {}, max speed: {}, total miles: {}".format(self.price,self.max_speed,self.miles)
        return self
    def ride(self):
        self.miles += 10
        print "riding"
        return self
    def reverse(self):
        self.miles -= 5
        print "reversing"
        return self
        
#now create an instance of the class
new_bike_1 = Bike(100,"15mph")
new_bike_1.ride().ride().ride().reverse().displayInfo()
new_bike_2 = Bike(200,"25mph")
new_bike_2.ride().ride().reverse().reverse().displayInfo()
new_bike_3 = Bike(300,"35mph")
new_bike_3.reverse().reverse().reverse().displayInfo()