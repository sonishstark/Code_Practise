x = float(input("Enter the value: "))
y = float(input("Enter the value: "))

z =  round(x + y)
#built in way to print numbers with comma
print(f"{z:,}")

d = round(x / y, 2)
#buitl in funcitons to print with decimal 
print(f"{d:.2f}")