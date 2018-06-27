class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def display_health(self):
        print "name: {}, health: {}".format(self.name,self.health)
        return self
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self

class Dogs(Animal):
    def pet(self):
        self.health += 5
        return self
      
class Dragon(Animal):
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print "I am Drago"
        return self

#my_Animal = Animal("Cat",9).walk().walk().walk().run().run().display_health()
#my_dog = Dogs("Duncan",150).walk().walk().walk().run().run().pet().display_health()
#my_drago = Dogs("Dragon",170).walk().walk().walk().run().run().pet().display_health() - runs parent diplay health only
#my_Animal = Animal("Cat",9).pet() - failed pet method is not a method of animal class
#my_Animal = Animal("Cat",9).fly() -  failed fly method is not a method of animal class
#my_Animal = Animal("Cat",9).display_health()


