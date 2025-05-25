# PRIVATE AND PROTECTED VARIABLE, SUPER() FUNC, ABSTRACT CLASSES AND METHODS, INSTANCE METHODS, CLASS METHODS, DUNDER METHODS



# Accessing and Modifying Attributes
# Class attributes can be accessed using the class name or an instance of the class.
# Instance attributes can only be accessed using an instance of the class.
# Modifying a class attribute through an instance creates a new instance attribute with the same name, shadowing the class attribute.

# The __dict__ Attribute
# Every class and instance in Python has a __dict__ attribute, which is a dictionary that stores the attributes 
# and their values. This is a useful way to inspect the attributes of a class or object.


# public variable is the other name of instance variable

# Protected Variables
# Should only be accessed within the class and its subclasses.
# Indicated by a single underscore _ before the variable name.
# This is just a convention; it's not strictly enforced by Python.

# ✅ Example:

# class Car:
#     def __init__(self):
#         self._engine = "V8"  # Protected variable
# class SportsCar(Car):
#     def show_engine(self):
#         return self._engine  # ✅ Accessible in subclass

# car = Car()
# print(car._engine)  # ⚠️ Accessible, but discouraged (Python allows it)


# 🔒 Private Variables
# Strictly not accessible outside the class.
# Indicated by two underscores __ before the variable name.
# Python name-mangles it internally to prevent external access.

# ✅ Example:

# class Car:
#     def __init__(self):
#         self.__chassis_number = "XYZ123"  # Private variable

# car = Car()
# # print(car.__chassis_number)  ❌ Error: not accessible directly
# print(car._Car__chassis_number)  # ✅ Name mangling allows access (not recommended)


# Here are the main use cases for the super() function:

# 1. Accessing a method from the parent class
# When you want to call a method of a parent class from a subclass without explicitly referencing the parent class by name.

# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def greet(self):
#         super().greet()  # Call Parent class's greet method
#         print("Hello from Child")

# c = Child()
# c.greet()
# Output:
# Hello from Parent
# Hello from Child


# 2. Calling the constructor of the parent class
# The super() function can be used to call the constructor (__init__) of the parent class to initialize attributes
#  defined in the parent class when you're overriding the __init__ method in the child class.


# class Parent:
#     def __init__(self, name):
#         self.name = name

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Call Parent's constructor
#         self.age = age

# c = Child("John", 25)
# print(c.name)  # Access Parent's attribute
# print(c.age)   # Access Child's attribute
# Output:
# John
# 25



# 🔍 Abstract Classes and Methods in Python
# In Object-Oriented Programming (OOP), abstract classes and abstract methods are used to define a blueprint for other classes.
# They cannot be instantiated directly and are meant to be inherited.

# 🧱 Abstract Class
# An abstract class is a class that contains one or more abstract methods. It is defined using the ABC module.
# You cannot create objects of an abstract class.
# It is used to enforce that derived classes implement specific methods.

# 🔧 Abstract Method
# An abstract method is a method that is declared in the abstract class but does not have any implementation (no body). 
# Subclasses must override it.

# ✅ How to Define Abstract Class and Method

# from abc import ABC, abstractmethod

# class Animal(ABC):  # Abstract class
#     @abstractmethod
#     def make_sound(self):  # Abstract method
#         pass
# 👇 Now, any subclass must implement make_sound():

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# # dog = Animal()  ❌ Error: Can't instantiate abstract class
# dog = Dog()        # ✅ Works
# dog.make_sound()   # Output: Woof!



# 🧠 What Are Instance Methods in Python?
# Instance methods are functions defined inside a class that operate on an instance (object) of that class. 
# These methods can access and modify the object's attributes using the self parameter.

# ✅ Characteristics of Instance Methods:
# Defined inside a class
# First parameter is always self (refers to the current object)
# Can access or modify instance variables
# Called using object name (e.g., obj.method())

# 📦 Example:

# class Person:
#     def __init__(self, name):
#         self.name = name  # instance variable

#     def greet(self):  # instance method
#         print(f"Hello, my name is {self.name}")

# p1 = Person("Ayesha")
# p1.greet()  # Output: Hello, my name is Ayesha



# In Python, class methods are methods that are bound to the class, not the instance. They are used when you want
#  to access or modify the class state (not instance-specific data). You define a class method using the @classmethod decorator.

# 🔑 Key Points:
# They take cls as the first parameter, which refers to the class itself (similar to how instance methods take self).
# Useful for creating alternative constructors or working with class variables.
# Can be called using the class name or an instance.

# ✅ Syntax:

# class MyClass:
#     class_variable = 0

#     @classmethod
#     def my_class_method(cls):
#         cls.class_variable += 1
#         print(f"Updated class_variable: {cls.class_variable}")
# 📦 Example:

# class Student:
#     school = "Green Valley High"  # class variable

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school

# s1 = Student("Ali")
# s2 = Student("Sara")

# print(s1.school)  # Green Valley High
# Student.change_school("Blue Hill School")
# print(s2.school)  # Blue Hill School





# Dunder methods (short for **"double underscore" methods**, also known as **magic methods** or **special methods**) are a key part of Python's Object-Oriented Programming (OOP). They start and end with double underscores, like `__init__`, `__str__`, `__len__`, etc. These methods allow developers to **customize the behavior of Python's built-in operations** (such as printing, addition, iteration, etc.) for user-defined classes.

# ## 🔍 **Why are they called "Dunder" methods?**

# **Dunder** = **D**ouble **UNDER**score
# Example: `__init__` is read as "dunder init".

# ## 🧠 **Core Purpose of Dunder Methods in OOP:**

# They allow objects to:

# * Initialize themselves
# * Behave like built-in types
# * Be used in expressions like `+`, `-`, `==`, etc.
# * Be iterable, callable, printable, etc.

# ## 🔑 Categories of Dunder Methods

# ### 1. **Object Construction & Representation**

# | Dunder Method         | Purpose                              | Example                                     |
# | --------------------- | ------------------------------------ | ------------------------------------------- |
# | `__init__(self, ...)` | Constructor, initializes object      | Called automatically when object is created |
# | `__new__(cls, ...)`   | Allocates memory (rarely overridden) | Runs before `__init__`                      |
# | `__del__(self)`       | Destructor                           | Called when object is deleted               |
# | `__str__(self)`       | String representation for users      | Used by `print(obj)`                        |
# | `__repr__(self)`      | Official string for developers       | Used in `repr(obj)`                         |

# ### 2. **Operator Overloading**

# Let objects behave with operators like `+`, `-`, `*`, `==`, etc.

# | Operator | Dunder Method              | Example        |
# | -------- | -------------------------- | -------------- |
# | `+`      | `__add__(self, other)`     | `obj1 + obj2`  |
# | `-`      | `__sub__(self, other)`     | `obj1 - obj2`  |
# | `*`      | `__mul__(self, other)`     | `obj1 * obj2`  |
# | `/`      | `__truediv__(self, other)` | `obj1 / obj2`  |
# | `==`     | `__eq__(self, other)`      | `obj1 == obj2` |
# | `<`      | `__lt__(self, other)`      | `obj1 < obj2`  |

# ### 3. **Type Conversion**

# | Dunder            | Use                               |
# | ----------------- | --------------------------------- |
# | `__int__(self)`   | Converts object to `int`          |
# | `__float__(self)` | Converts object to `float`        |
# | `__bool__(self)`  | Converts object to `True`/`False` |

# ### 4. **Attribute Access**

# | Dunder                           | Purpose                               |
# | -------------------------------- | ------------------------------------- |
# | `__getattr__(self, name)`        | Called when an attribute is not found |
# | `__getattribute__(self, name)`   | Called for **every** attribute access |
# | `__setattr__(self, name, value)` | Custom behavior for `obj.attr = val`  |
# | `__delattr__(self, name)`        | For `del obj.attr`                    |

# ### 5. **Callable and Context Managers**

# | Dunder                                      | Purpose                                  |
# | ------------------------------------------- | ---------------------------------------- |
# | `__call__(self, ...)`                       | Makes an object callable like a function |
# | `__enter__(self)`                           | Used in `with` statement                 |
# | `__exit__(self, exc_type, exc_val, exc_tb)` | Cleans up after `with` block             |

# ### 6. **Container/Iterable Behavior**

# | Dunder                          | Behavior                        |
# | ------------------------------- | ------------------------------- |
# | `__len__(self)`                 | Enables `len(obj)`              |
# | `__getitem__(self, key)`        | Enables `obj[key]`              |
# | `__setitem__(self, key, value)` | Enables `obj[key] = value`      |
# | `__delitem__(self, key)`        | Enables `del obj[key]`          |
# | `__iter__(self)`                | Returns iterator                |
# | `__next__(self)`                | Returns next value in iteration |

# ### 7. **Miscellaneous**

# | Dunder                     | Purpose                                     |
# | -------------------------- | ------------------------------------------- |
# | `__contains__(self, item)` | Enables `item in obj`                       |
# | `__reversed__(self)`       | Supports `reversed(obj)`                    |
# | `__hash__(self)`           | Makes object hashable for use in sets/dicts |

# ## 💡 Example: Operator Overloading Using Dunder Methods
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# print(p1 + p2)  # (4, 6)
