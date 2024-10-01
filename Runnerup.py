if __name__ == '__main__':
    n = int(input())
    #constrain
    if 2 <= n <= 10:
    #getting inputs as a list in array    
      arr = list(map(int, input().split()))
      #checking the values in the arrays are matching the constrain
      for i in arr:
          #constrain
          if not -100 <= i <= 100:
              exit()
               
    highest_arr = max(arr) #storing the highest value by max inbuilt function
    filtered_arr = [i for i in arr if i != highest_arr] #storing all the numbers except the highest 
    runner_up = max(filtered_arr) #filtering the highest of that stored numbers
    print(runner_up) 