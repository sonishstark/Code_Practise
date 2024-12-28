#global variables
x = int(input("Enter a value of X: "))
y = int(input("Enter a value of Y: "))

def conditional_1():

    if x < y:
        print("X is less than Y")
    elif x > y:
        print("X is greater than Y")
    else:
        print("X is equal to Y")

#conditional_1()

def conditional_2():
    
    if x > y or x < y:
        print("X is not equal to Y")
    else:
        print("X is equal to Y")

conditional_2()
