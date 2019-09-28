# A List is a collection which is ordered and changeable. Allows duplicate members. Similar to an array in JS.

# Create list - 0 based
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
#numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])  # Oranges

# Get length
print(len(fruits))

# Append to list - adds to the end of the list/array
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'  # replaced apples which was in the [0] position

# Remove with pop - by position
fruits.pop(2)

# Reverse list - last to first
fruits.reverse()

# Sort list - in alphabertical order
fruits.sort()

# Reverse sort - ^^ in opposite order - descending alphabetical order
fruits.sort(reverse=True)

print(fruits)
