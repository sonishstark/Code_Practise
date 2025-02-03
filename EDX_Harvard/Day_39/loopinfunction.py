def main():
    number = get_number()
    meow(3)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            return n

def meow(n):
    for i in range(n):
        print("meow")

main()
<<<<<<< HEAD
#29
=======
#31
>>>>>>> 75248ebf2704b5daaf764f0b4c7fe570d6303160


