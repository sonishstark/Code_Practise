class Person:
    #constructor
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John smith")
john.talk()