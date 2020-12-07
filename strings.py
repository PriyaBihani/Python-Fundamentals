# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Priya"
age = 18

# Concatenate
print('Hello I am ' + name + " and I am " + str(age) + " years old")

# String Formatting

# Arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {name} and i am {age} years old'.format(name=name, age=age))

# F-Strings (only in 3.6+)
print(f'My name is {name} and i am {age}')

# String Methods

s = "hello there world"

# Capitalize first letter
print(s.capitalize())

# Make All Upper case
print(s.upper())
print(s.lower())

# Swap Case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sun = "H"
print(s.count(sub))