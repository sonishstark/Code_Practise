# try is used to avoid crashing of the program
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age) 
    #if you enter a wrong input it prints the below
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('invalid value')
    

