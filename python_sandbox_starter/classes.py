# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class


class User:
    # Constructor - function that runs when you instantiate an object from a class
    def __init__(self, name, email, age):  # self is this
        self.name = name
        self.email = email
        self.age = age
    # methods

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extend class


class Customer(User):
  # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        # new property
        self.balance = 0
    # methods

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init user object
harjoth = User('Harjoth Khara', 'harj@gmail.com', 32)

# print(type(harjoth))  # <class '__main__.User'>
# telling us that this is a user object

# print(harjoth.age)  # 32

# Init customer
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

harjoth.has_birthday()
print(harjoth.greeting())
