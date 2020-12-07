# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dict
person = {
    'first_name': 'Jhon',
    'last_name': 'Doe',
    'age' : 30
}

# Using a construct
# person = dict(
#     first_name = 'Jhon',
#     last_name = 'DOe',
#     age = 30
# )

# Access value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '7982776083'

# Get keys
print(person.keys())

# Get items
print(person.items())

# Make a copy
person2 = person.copy()
person2['city'] = 'Boston'
# print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get Length
print(len(person2))

print(person)

# A list of dictionaries

people = [
    {'name': 'Priya', 'age': 18},
    {'name': 'Kartik', 'age': 20}
]
print(people[1]['name'])