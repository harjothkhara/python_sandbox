# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate

#print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
#print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+) - similar to JS template literals, instead of backticks we put an f, and don't use $
#print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize string - first letter is capitalized
# print(s.capitalize())

# Make all uppercase
# print(s.upper())

# Make all lower
# print(s.lower())

# Swap case
# print(s.swapcase())

# Get length
# print(len(s))

# Replace
#print(s.replace('world', 'everyone'))

# Count - e.g count the number of h's inside the string
#sub = 'h'
# print(s.count(sub))

# Starts with - returns true or false value based on how it starts
# print(s.startswith('hello')) # true - our string does start with 'hello'

# Ends with - returns true or false based on what string ends with
# print(s.endswith('d'))

# Split into a list - take our string and turn it into a list, an array. it'll have all the words in the list
# print(s.split())  # ['hello', 'world']

# Find position - find a position of a character, 0 based, first character if multiple in string.
# print(s.find('r')) # 8

# Is all alphanumeric - return true or false if all values are alphanumeric
# print(s.isalnum())  # false b/c of space in string otherwise true

# Is all alphabetic - return true or false if all values alphabetic
# print(s.isalpha()) # false b/c of space in string otherwise true

# Is all numeric - return true or false if all values numeric
# print(s.isnumeric())  # false
