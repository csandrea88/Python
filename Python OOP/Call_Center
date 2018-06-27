class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.tax = 0
    def Display_info(self):
        #print "price: {}".format(self.price)
        print "price: {}, item: {}, weight: {}, brand: {}, status {}".format(self.price,self.item_name,self.weight,self.brand,self.status)
        return self
    def Sell(self):
        self.status = "sold"
        return self
    def Add_tax(self, tax):
        self.price *= (1+tax)
        return self
    def Return(self,reason):
        if reason == "defective":
            self.price = 0
            self.status = "defective"
        elif reason == "used":
            self.price *= .80
            self.status = "used"
        elif reason == "likenew":
            self.status = "for sale" 
        return self

        
#now create an instance of the class
new_Product_1 = Product(50,"jeans",".5lbs","Levis").Display_info()
new_Product_1.Sell().Display_info()
new_Product_1.Add_tax(.10).Display_info()
new_Product_1.Return("defective").Display_info()
new_Product_2 = Product(100,"sweater",.25,"Macys").Display_info()
new_Product_2.Add_tax(.10).Display_info()
new_Product_2.Return("used").Display_info()
new_Product_3 = Product(150,"boots",.75,"Klein").Display_info()
new_Product_3.Return("likenew").Display_info()
