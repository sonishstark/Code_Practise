def greet1(input):
    if "hello" in input:
        print("hello, there")
    else:
        print("I'm not sure what you mean")
        
#you can assign usercase input, even inside the while calling the funciton
greet1(input = input("Enter an sentence for greet 1: "))

def greet2(input):
    if "hello" in input:
        return("hello, there")
    else:
        return("I'm not sure what you mean")
#an return statement always need to be stored somewhere Ex: in a variable
greeting = greet2(input = input("Enter an sentence greet 2: "))
#you can edit input statement when there is variable that you are printing
print("Hm, " + greeting)