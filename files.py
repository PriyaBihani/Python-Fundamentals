# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get Some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('Heyaaaa')
myFile.write('  Heloooo')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' Hello frannnds')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(10)
print(text)
