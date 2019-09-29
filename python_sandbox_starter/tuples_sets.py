# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')  # ('Apples', 'Oranges', 'Grapes')
# Using a constructor
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)  # leaving a trailing comma or it will be a string
# print(fruits2, type(fruits2)) # ('Apples',) <class 'tuple'>

# Get value
print(fruits[1])  # Oranges

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# print(fruits2) # deleted fruits2 above so no longer defined

print(len(fruits))  # 3


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set - True or False
print('Apples' in fruits_set)  # True

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete - same as not defining it
del fruits_set

print(fruits_set)  # NameError: name 'fruits_set' is not defined
