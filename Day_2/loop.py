if __name__ == '__main__':
    n = int(input().strip())
    #constrain
    if  1 <= n <= 20:
        #how to enter for loop and i is incremented by default
        for i in range(n):
            print(i**2)