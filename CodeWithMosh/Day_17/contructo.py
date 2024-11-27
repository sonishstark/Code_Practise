class Person:
    #constructor
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print("talk")


john = Person("John smith")
print(john.name)
john.talk