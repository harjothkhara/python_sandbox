# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# similar to an object literal in JS

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# constructor
#person2 = dict(first_name='Sara', last_name='Williams')
#print(person2, type(person2))

# Get value
print(person['first_name'])  # common way
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-555'

# Get dict keys
print(person.keys())

# Get dict items
# dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 30), ('phone', '555-555-555')])
print(person.items())

# Copy dict - similar to spread operator in JS
person2 = person.copy()
person2['city'] = 'Boston'
# print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear - empty dictionary {}
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]
print(people, people[1]['name'])
