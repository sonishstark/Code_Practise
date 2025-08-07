def greet1(user_input):
    if "hello" in user_input.lower():
        print("hello is present in the input")
    else:
        print("hello is not present in the input")

def greet2(user_input):
    if "hello" in user_input.lower():
        # can return a string value instead of printing
        return "hello is present in the input"
    else:
        return "hello is not present in the input"

def main():
    # First greeting using print inside the function
    user_text1 = input("Enter a sentence for greet1: ")
    # can directly pass as a paramtereized function
    greet1(user_text1)

    # Second greeting using return value stored in a variable
    user_text2 = input("Enter a sentence for greet2: ")
    # can pass the return value to a variable
    greeting = greet2(user_text2)
    print("Hm, " + greeting)

# Ensures the script only runs when executed directly
if __name__ == "__main__":
    main()