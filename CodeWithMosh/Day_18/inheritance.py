class Mammal:
    def walk(self):
        print("Cat walk is ")
        

class Dog(Mammal):
    pass #class in python cannot be empty 


class Cat(Mammal):
    def be_annoying(self):
        print("annonying")

#calling object    
dog1 = Dog()
dog1.walk()
#you can call mutiple methods using objects
cat1 = Cat()
cat1.be_annoying()

    
    
    