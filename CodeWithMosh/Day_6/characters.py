name = input('Enter the name: ')
length = len(name)

if length < 3:
    print('The name must must be atleast 3 characters')
elif length > 50:
    print('The name must be less than 50 characters')
else:
    print("The name has correct characters")