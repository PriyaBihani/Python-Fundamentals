# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'

    def hasBirthday(self):
        self.age += 1


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance


# INIT user Object
priya = User('Priya Bihani', 'priyabihani123@gmail.com', 18)
brad = User('Brad Traversy', 'bradtraversy123@gmail.com', 38)

# Edit Property
priya.age = 20

print(priya.name)

priya.hasBirthday()

# Call method
print(priya.greeting())

# Init customer
john = Customer('Jhone Doe', 'jhon@gmail.com', 40)
john.setBalance(1000)
