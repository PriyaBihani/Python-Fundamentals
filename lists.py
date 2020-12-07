# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
# numbers = [1, 2, 3, 4, 5]

# Using a constructor
numbers = list((1, 2, 3, 4))
print(type(numbers))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# Get value
print(fruits[1])

# Get len
print(len(fruits)) 

# Append to list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'strawberries')

# Remive from position
fruits.pop(3)

# Reverse List
fruits.reverse()

# Sort List
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)


