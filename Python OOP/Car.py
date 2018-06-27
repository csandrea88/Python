class Car(object):
    def __init__(self, price, speed, fuel, mileage,tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        self.display_all()
    def display_all(self):
        print "price: {}, speed: {}, fuel: {}, mileage: {}, tax: {}".format(self.price,self.speed,self.fuel,self.mileage,self.tax)
        return self
   
        
#now create an instance of the class
new_car_1 = Car(2000,"35mph","Full", "15mpg",0.12)
new_car_2 = Car(2000,"5mph","Not Full", "105mpg",0.12)
new_car_3 = Car(2000,"15mph","Full", "95mpg",0.12)
new_car_4 = Car(2000,"25mph","Full", "25mpg",0.12)
new_car_5 = Car(2000,"45mph","Full", "15mpg",0.12)
new_car_6 = Car(20000000,"35mph","Empty", "15mpg",0.15)