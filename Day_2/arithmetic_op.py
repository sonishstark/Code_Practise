if __name__ == '__main__':
    a = int(input())
    b = int(input())
    #learned how to type power operator ("(^)" into "(**)") to an integer
    if 1 <= a <= 10**10 or 1<= b <= 10**10:
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("Constrain not satisfied")