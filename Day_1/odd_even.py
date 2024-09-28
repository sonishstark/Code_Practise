if __name__ == '__main__':
    n = int(input().strip())
#checking even or odd    
    if n % 2 != 0:
        print("Weird")
#learned to write the range between ex: 2 to 5
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
     