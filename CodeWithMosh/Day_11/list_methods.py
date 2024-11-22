numbers =[5, 4, 3, 2, 20, 11]
#copy of a list
numbers_copy = numbers.copy()
#inbuilt funcitons to add a number in the list
numbers.append(13)
print(numbers)
#inbuilt funcitons to add a number in the sepcific position in a list
numbers.insert(1, 23)
print(numbers)
numbers.remove(5)
print(numbers)
#prints the index of that located number
print(numbers.index(3))
numbers.sort()#ascending order
print(numbers)
numbers.reverse()#then reverse it so you get descending order
print(numbers)
