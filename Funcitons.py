def is_leap(year):
    leap = False
    #both if statements are constrain 
    if 1900 <= year <= 10**5:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap = True
    return leap

if __name__ == '__main__':
    year = int(input("Enter a year: "))
    #is_leap(year) prints the final output of the whole function
    print(is_leap(year))
