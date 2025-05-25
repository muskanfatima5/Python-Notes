# PROPERTY DECORATORS: @property, @setter, and @deleter, callable() and __call__(), CUSTOM EXCEPTION, ITERATION, CUSTOM CLASS ITERABLE

# In Python's Object-Oriented Programming (OOP), property decorators like @property, @<property_name>.setter, and @<property_name>.deleter are used to manage attributes with getter, setter, and deleter methods — in a clean, Pythonic way.
# They help encapsulate instance variables and provide controlled access.

# 🔑 1. @property — Getter
# This turns a method into a read-only property.

# class Student:
#     def __init__(self, marks):
#         self._marks = marks

#     @property
#     def marks(self):
#         return self._marks

# Now you can access .marks like an attribute, even though it's a method:
# s = Student(90)
# print(s.marks)   # prints: 90 (calls the getter method behind the scenes)


# 🖊️ 2.@<property>.setter — Setter
# This allows you to set a value to the property with validation or control logic.

# class Student:
#     def __init__(self, marks):
#         self._marks = marks

#     @property
#     def marks(self):
#         return self._marks

#     @marks.setter
#     def marks(self, value):
#         if value < 0:
#             raise ValueError("Marks can't be negative")
#         self._marks = value

# Now you can assign a value with validation:
# s = Student(90)
# s.marks = 95      # calls setter
# print(s.marks)    # 95
# s.marks = -10     # ❌ raises ValueError


# ❌ 3. @<property>.deleter — Deleter
# This lets you define what should happen when a property is deleted using del.

# class Student:
#     def __init__(self, marks):
#         self._marks = marks

#     @property
#     def marks(self):
#         return self._marks

#     @marks.deleter
#     def marks(self):
#         print("Deleting marks...")
#         del self._marks

# s = Student(90)
# del s.marks       # prints "Deleting marks..."


# 🔁 Summary Table
# | Decorator         | Purpose                    | Syntax                   |
# | ----------------- | -------------------------- | ------------------------ |
# | `@property`       | Getter (read value)        | `@property` above method |
# | `@<prop>.setter`  | Setter (write value)       | `@marks.setter`          |
# | `@<prop>.deleter` | Deleter (delete attribute) | `@marks.deleter`         |


# 🔹 callable(object) — Built-in Function
# ✅ What It Does:
# Checks if an object can be called like a function.

# 🔹 Syntax:

# callable(object)
# 🔹 Returns:
# True → if the object can be called (like functions, methods, or objects with __call__()).

# False → otherwise.

# 🔹 Example:

# print(callable(len))          # True (built-in function)
# print(callable("hello"))      # False (string isn't callable)


# 🔹 __call__() — Special Method
# ✅ What It Does:
# Lets you make class instances behave like functions.

# 🔹 When used:
# If a class defines a __call__() method, its instances can be called like functions.

# 🔹 Example:

# class Greet:
#     def __call__(self, name):
#         return f"Hello, {name}!"

# g = Greet()
# print(callable(g))        # True
# print(g("Alice"))         # Calls g.__call__("Alice")

# ✅ Real-World Use Case
# Function-like Objects

# class Multiplier:
#     def __init__(self, factor):
#         self.factor = factor

#     def __call__(self, value):
#         return value * self.factor

# double = Multiplier(2)
# print(double(5))   # 10
# print(callable(double))  # True

# 🔁 Summary Table
# | Concept         | Meaning                                  | Usage Example                  |
# | --------------- | ---------------------------------------- | ------------------------------ |
# | `callable(obj)` | Checks if an object can be called        | `callable(my_obj)`             |
# | `__call__()`    | Makes an object callable like a function | `obj()` calls `obj.__call__()` |



# 💥 What is a Custom Exception in OOP (Python)?
# A custom exception is a user-defined error class that inherits from Python’s built-in Exception class (or any of its subclasses). 
# It's used to represent specific error situations in your program that are not covered by standard exceptions like ValueError, TypeError, etc.

# 🔧 Why Use Custom Exceptions?
# To make error messages more meaningful
# To handle domain-specific errors (e.g., "NegativeSalaryError", "InvalidGradeError")
# To make code cleaner, more readable, and maintainable

# class NegativeValueError(Exception):
#     def __init__(self, value):
#         self.value = value
#         super().__init__(f"Negative value error: {value} is not allowed.")

# def set_age(age):
#     if age < 0:
#         raise NegativeValueError(age)
#     print(f"Age set to {age}")

# # Test
# set_age(25)       # ✅ OK
# set_age(-5)       # ❌ Raises NegativeValueError

# OUTPUT
# Age set to 25
# Traceback (most recent call last):
# ...
# NegativeValueError: Negative value error: -5 is not allowed.

# 🧱 Structure of Custom Exception
# class CustomError(Exception):  # Inherit from Exception
#     def __init__(self, message):
#         super().__init__(message)  # Call parent constructor


# Summary
# | Feature        | Explanation                        |
# | -------------- | ---------------------------------- |
# | Inherits from  | `Exception` or its subclasses      |
# | Purpose        | Represent domain-specific errors   |
# | Custom Message | Yes, through `__init__()`          |
# | Raising it     | `raise CustomError("message")`     |
# | Handling it    | `try` / `except CustomError as e:` |






# ## 🔁 What is *Iteration* in OOP?

# In general, **iteration** refers to the process of going through a collection (like a list, tuple, dictionary, etc.) 
# item by item — usually using a `for` loop.
# In **Object-Oriented Programming (OOP)**, *iteration* becomes more powerful and flexible because
#  **you can make your own objects iterable** by implementing special methods.

# ## 🧠 What Makes an Object Iterable?
# In Python, an object is **iterable** if it implements the `__iter__()` method, which returns an **iterator**. An iterator is an object that implements the `__next__()` method.

#🔹 Two Key Concepts:
# * **Iterable** = something you can loop over (`list`, `tuple`, `set`, etc.)
# * **Iterator** = object that remembers its state as you traverse it and implements:

#   * `__iter__()` → returns itself
#   * `__next__()` → returns the next item or raises `StopIteration`

#🔧 How to Create an Iterable Class (OOP Style)

# Here’s a practical OOP example:
# ✅ Example: A custom range-like class

# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         self.current = self.start
#         return self

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         else:
#             current = self.current
#             self.current += 1
#             return current

#💡 Usage:

# for num in MyRange(1, 5):
#     print(num)

# **Output:**
# 1
# 2
# 3
# 4

# 🧱 Why is Iteration Useful in OOP?

# 1. **Encapsulation**: You can define how your objects should be looped over.
# 2. **Custom Behavior**: You can create complex logic for what "next" means.
# 3. **Lazy Evaluation**: With iterators/generators, you don’t need to store all data at once.
# 4. **Integration with Pythonic Features**: Iterable classes work with loops, list comprehensions, `in`, `sum()`, `max()`, etc.

# 🔁 Bonus: Iterable vs Generator
# * Iterable: Implements `__iter__()` and returns an iterator.
# * Generator: Special kind of iterator that uses `yield` and automatically handles state.






# In Python's Object-Oriented Programming (OOP), a custom class iterable is a user-defined class that you make iterable
#  — meaning you can loop over its instances using a for loop or use it with functions like list(), sum(), etc.

# ✅ To make a custom class iterable, your class must implement:
# __iter__(self) — This should return an iterator object (often self).
# __next__(self) — This returns the next item in the sequence and raises StopIteration when the sequence ends.


# class CountUpto:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 1

#     def __iter__(self):
#         return self  # returning iterator object

#     def __next__(self):
#         if self.current <= self.limit:
#             num = self.current
#             self.current += 1
#             return num
#         else:
#             raise StopIteration


# for num in CountUpto(5):
#     print(num)

# OUTPUT
# 1
# 2
# 3
# 4
# 5
