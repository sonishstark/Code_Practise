#passing the name in the function
def hello(to):
    print(f"hello, {to}")

def main():
    name = input("What's your name: ")
    #adding the name through the user input
    hello(name)
main()
