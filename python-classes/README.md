
# Python Classes

## Introduction

Classes are blueprints for creating objects that encapsulate data (attributes) and behavior (methods).

They provide a way to model real-world entities and organize code in a structured, reusable manner.
## Key Concepts

Creating a Class:

Python
class ClassName:
    # Class body

Attributes:

Data associated with a class and its instances.

Defined within the __init__() method (constructor).

Accessed using dot notation: object.attribute

Methods:

Functions defined within a class that operate on its data.

Also invoked using dot notation: object.method()

Instances:

Individual objects created from a class.

Each instance has its own unique set of attribute values.
## Basic Example:

Python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")
## Usage:

Python
my_dog = Dog("Fido", "Labrador")
print(my_dog.name)  # Output: Fido
my_dog.bark()      # Output: Woof!
## Additional Features

Inheritance: Classes can inherit attributes and methods from other classes.
Special Methods: Built-in methods like __str__() and __repr__() for string representation.
Class Attributes: Attributes shared by all instances of a class.
## Resources

Official Python Tutorial on Classes: https://docs.python.org/3/tutorial/classes.html

Real Python Guide to Python Classes: https://realpython.com/python-classes/

Learn Python: Classes: https://www.learnpython.org/en/Classes_and_Objects
