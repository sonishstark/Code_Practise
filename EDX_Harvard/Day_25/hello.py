def main():
    name = input("What's your name: ")
    #adding the name through the user input
    hello(name)
    
#passing the name in the function
def hello(to):
    print("hello,", to)

main()
