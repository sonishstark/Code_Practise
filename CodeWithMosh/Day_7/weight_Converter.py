weight = float(input('Enter your weight: '))
unit = input('(L)bs or (K)gs: ')

if unit.lower() == 'l':
    print(f"you are {weight * 0.45} kilograms")
elif unit.lower() == 'k':
    print(f"you are {weight / 0.45} pounds")
else:
    print("invalid input")

    
