 # Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at index 1 (second position)
my_list.insert(1, 15)

# Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of value 30
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")

# Print the final list to see the result
print(f"Final list: {my_list}")
