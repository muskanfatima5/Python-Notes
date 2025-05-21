# What is a Decorator in Python?
# A decorator is a function that adds extra features to another function or method, without changing its original code.

# 🧾 Think of it like:
# "Adding chutney to samosa – the samosa is the same, but now it's tastier!"

# 🔧 Basic Decorator Function
# Here’s a simple example:

# def chutney_decorator(samosa_function):
#     def wrapper():
#         print("Adding green chutney!")
#         samosa_function()
#     return wrapper

# @chutney_decorator
# def serve_samosa():
#     print("Samosa is served.")

# serve_samosa()

# Output:

# Adding green chutney!
# Samosa is served.

# 📌 @chutney_decorator tells Python to wrap the original function with some extra behavior.


# 👨‍🏫 What are Class Method Decorators?
# Python provides special decorators for use inside classes. These change how methods behave.

# 📌 1. @staticmethod
# It’s a method that does not take self or cls.
# Acts like a regular function inside a class.
# Can be called directly using the class or object.

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# Math.add(5, 3)  # Output: 8

# 📌 Use when your method doesn’t need to access instance or class variables.

# 📌 2. @classmethod
# Takes cls as its first argument.
# Works with the class itself, not the instance.
# Can modify class-level variables.

# class ShoppingList:
#     items = []

#     @classmethod
#     def add_item(cls, item):
#         cls.items.append(item)
# 📌 Use when you want to work with class-level data or create alternative constructors.

# 📌 3. @property
# Used to turn a method into a read-only attribute.
# Lets you access methods like attributes, without parentheses.

# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
# 📌 Use when you want to control access to attributes (like getters).

# 🎛️ Custom Decorator with Parameters
# You can even create decorators that take arguments!

# def spice_level(level):
#     def decorator(func):
#         def wrapper():
#             print(f"Spice level: {level}")
#             func()
#         return wrapper
#     return decorator

# @spice_level("high")
# def make_curry():
#     print("Curry is ready!")


# 📚 Summary Table
# Decorator	            What it Does	                           When to Use
# @staticmethod	        Regular function inside class, no self	   For utility/helper methods
# @classmethod	        Uses cls, works with class-level data	   To change or access class data
# @property	            Turns method into a read-only attribute	   For attribute-style access to methods
# Custom Decorator	    Adds extra behavior to function/method	   For logging, timing, validation etc.