##remove spaces inbuilt functions 
name = "  sonish sasidharan  ".strip().title()

#the last argument ends the curson moving to next line
print("Hello,",name, end="")
print(" how are you")

#printing removed spaces and capitalized user name 
print(f"hello, {name}")
#splitting name
first, last = name.split()
print(f"hello, {first}")
print("hi")