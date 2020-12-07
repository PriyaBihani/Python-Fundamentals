# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Simple Tuple
fruit_tuple = ('Apple', 'Orange', 'Mango') 

# Using Constructor
# fruit_tuple = (('Apple', 'Orange', 'Mango'))

# Get single value
print(fruit_tuple[1])

# Can not change value
# fruit_tuple[1] = 'Grape'

# Tuples with one value should leave a trailaing comma
fruit_tuple2 = ('Strawberry',)

del fruit_tuple2

# Get length of tuple
print(len(fruit_tuple))


# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_set = {'Apple', 'Orange', 'Mango'}

# Check if in a set
print('Apple' in fruit_set)

# Add to set
fruit_set.add('Grape')

# Remove to set
fruit_set.remove('Grape')

print(fruit_set)

# Clear set
fruit_set.clear()

# Delete set
del fruit_set