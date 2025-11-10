def get_guess():
    #variables inside the functions can be same name and different values
    guess = int(input("Enter a number: "))
    return guess

def main():
    #we can assign same variable, and a funciton to a variable
    guess = get_guess()
    print("The entered value is: ", guess)
    
def main2():
    guess = get_guess()
    #adding a conditional statement
    if guess == 50:
        print("Correct")
    else:
        print("Incorrect")
    
    
main()
