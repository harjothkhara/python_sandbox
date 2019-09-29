# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')  # created a file

# Get some info
print('Name: ', myFile.name)  # Name:  myfile.txt
# Is Closed :  False # means is it closed within our script
print('Is Closed : ', myFile.closed)  # False
print('Opening Mode: ', myFile.mode)  # Opening Mode:  w

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()
print('Is Closed : ', myFile.closed)  # True

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(6)  # read 6 characters
print(text)
