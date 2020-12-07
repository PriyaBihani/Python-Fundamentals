# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# x = 1
# y = 2.5
# name = 'Priya'
# is_cool = True

# Multiple assigment
x, y, name, is_cool = (1, 2.5, 'Priya', True )

# Print
print(x)

# Check type
print(type(x))

# Casting
x = str(x)
print(type(x))