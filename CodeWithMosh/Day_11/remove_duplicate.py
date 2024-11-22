duplicate = [11, 2, 55, 6, 6, 7, 7, 7, 8, 9, 109]
unique = list(set(duplicate))  # Convert to set to remove duplicates, then back to list
unique.sort()  # Sort the list to maintain order
print(unique)