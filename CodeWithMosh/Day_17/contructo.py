class Person:
    #constructor
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")

#object 1 for the same class
john = Person("John smith")
john.talk()

#object 2 for the same class
bob = Person("Bob smith")
bob.talk()