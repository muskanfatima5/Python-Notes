# BASIC OOP STRUCTURE, OBJECT, CLASS VARIABLES AND METHODS, PUBLIC VARIABLES AND METHODS, STATIC VARIABLES AND METHODS, CONSTRUCTOR AND DESTRUCTOR

# DEFINITION OF OOPS
# Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects 
# and classes, rather than functions and logic. An object is an instance of a class, which is a blueprint for creating objects. 


# Structure of a Basic OOP Assignment in Python:
# ✅ 1. Assignment Format (Simple Template)

# # Task: Create a class for a basic concept (e.g., Student, BankAccount, Employee)

# class ClassName:
#     def __init__(self, attribute1, attribute2):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2

#     def method1(self):
#         # some logic
#         pass

#     def display(self):
#         print(f"{self.attribute1} - {self.attribute2}")


# # Creating object
# obj1 = ClassName("value1", "value2")
# obj1.display()


# ✅ Step-by-Step: How to Create an Object in Python OOP
# 1. Define a Class
# A class is like a blueprint.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print(f"{self.name} got {self.marks} marks.")


# 2. Create an Object (also called Instance)
# Use the class name with brackets, passing any required values to the constructor:

# # Creating object
# s1 = Student("Ali", 92)
# s2 = Student("Sara", 88)
# Here:

# s1 and s2 are objects
# "Ali" and 92 are passed to the __init__() method
# Inside the class, self.name = "Ali" and self.marks = 92

# 3. Access Methods and Attributes
# Use the object to call class methods:

# s1.display()  # Output: Ali got 92 marks.
# s2.display()  # Output: Sara got 88 marks.


# 🧠 Think of it like this:
# class → Design of a car
# object → A real car made from that design



# ✅ 1. Class Variable (shared by all objects)
# A class variable is a variable that is shared across all instances (objects) of a class. It is defined inside the class but outside any method.

# 🧠 Think of it like:
# "One copy for the whole class."

# 🔹 Example:

# class Student:
#     school_name = "ABC High School"  # class variable

#     def __init__(self, name):
#         self.name = name  # instance variable

# s1 = Student("Ali")
# s2 = Student("Sara")

# print(s1.school_name)  # Output: ABC High School
# print(s2.school_name)  # Output: ABC High School
# If you change Student.school_name, it affects all objects unless they override it.

# ✅ 2. Class Method (marked with @classmethod)
# A class method is a method that works with the class itself, not with object instances. It uses cls instead of self.

# 🔹 Use Case:
# To access or modify class variables
# To create alternative constructors

# 🔹 Syntax:

# @classmethod
# def method_name(cls):
#     # code
# 🔹 Example:

# class Student:
#     school_name = "ABC High School"

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name

# Student.change_school("XYZ Grammar School")  # changes for all
# print(Student.school_name)  # Output: XYZ Grammar School


# ✅ 3. cls keyword
# Works like self, but for the class instead of the object.
# Used in class methods to refer to the class.
# 🔸 self → refers to instance/object
# 🔸 cls → refers to class




# ✅ What are Public Variables and Methods in Python?
# 🔓 Public = Open to Everyone
# Public variables and methods can be:
# Accessed from inside the class ✅
# Accessed from outside the class ✅ (using objects)
# By default, everything in Python is public unless you make it private or protected.

# 🔹 Example: Public Variable and Method

# class Student:
#     def __init__(self, name, marks):
#         self.name = name      # public variable
#         self.marks = marks    # public variable

#     def display(self):        # public method
#         print(f"{self.name} got {self.marks} marks.")

# Object creation
# s1 = Student("Ali", 90)

# Accessing public variables
# print(s1.name)      # ✅ Allowed
# print(s1.marks)     # ✅ Allowed

# Calling public method
# s1.display()        # ✅ Allowed
 

# Attributes are variables that belong to an object. They represent the object’s state or properties.
# Methods are functions that belong to an object. They define the object’s behavior.


# 🧠 How to Identify Public Members?
# No special symbol is used.

# self.name → public
# def display(self) → public method

# 🚫 Bonus Info: What's NOT Public?
# Just to understand the difference:

# Modifier	    Syntax	     Access level
# Public	    self.name	 Accessible everywhere ✅
# Protected	    self._name	 Convention: "internal use", not enforced 🚧
# Private	    self.__name	 Not directly accessible outside ❌



# ✅ Static Variables:
# A static variable (also called a class variable in many cases) is a variable that:
# Belongs to the class itself, not to any specific instance (object).
# Is shared across all instances of the class.
# Is typically defined inside the class but outside any method.
# In Python, a static variable can be accessed directly using the class name or through the object, but it's not tied to any specific object instance.

# ✅ Static Method:
# A static method is a method that:
# Does not require access to any instance or class-specific variables.
# Does not take self or cls as the first parameter.
# Can be called on both the class or instances without needing any object-specific data.
# To define a static method, we use the @staticmethod decorator.

# 📌 Key Points:
# Static methods are used for utility functions that don’t modify or need access to instance data or class-level data.
# Static variables are used when you want to store data shared by all instances of the class.

# 🔹 Syntax Example: Static Variables and Static Methods

# class Car:
#     # Static variable: Shared by all objects
#     total_cars = 0  # Static variable
    
#     def __init__(self, model):
#         self.model = model  # Instance variable
#         Car.total_cars += 1  # Increment static variable whenever an object is created

#     @staticmethod
#     def car_info():
#         print("This is a car class that manages car data.")
    
#     @classmethod
#     def car_count(cls):
#         print(f"Total cars created: {cls.total_cars}")

# Create instances
# car1 = Car("Toyota")
# car2 = Car("Honda")

# # Static method can be called directly from the class
# Car.car_info()

# # Class method can also access static variable
# Car.car_count()

# # Static variable accessed via class or instance
# print(Car.total_cars)    # Output: 2
# print(car1.total_cars)   # Output: 2


# When to Use Static Variables/Methods?
# Static Variable: When you want a variable shared across all instances of a class.
# Static Method: When you have a function that does not depend on instance or class variables (e.g., utility functions).

# 🔹 Real-World Example:

# class MathUtils:
#     # Static variable to track total calculations
#     total_calculations = 0

#     @staticmethod
#     def add(x, y):
#         MathUtils.total_calculations += 1
#         return x + y
    
#     @staticmethod
#     def subtract(x, y):
#         MathUtils.total_calculations += 1
#         return x - y

# # Call static methods
# print(MathUtils.add(5, 3))        # Output: 8
# print(MathUtils.subtract(10, 4))  # Output: 6

# # Access static variable
# print(f"Total calculations done: {MathUtils.total_calculations}")  # Output: 2



# 🏗️ Constructor in Python:
# A constructor is a special method that is automatically called when you create an object of a class.

# 📌 In Python, the constructor method is:

# def __init__(self):
# ✅ Purpose:
# To initialize object properties when an object is created.

# It sets the initial state of the object.

# 🔹 Example:

# class Student:
#     def __init__(self, name, marks):  # Constructor
#         self.name = name
#         self.marks = marks

# s1 = Student("Ali", 85)  # Constructor runs automatically
# print(s1.name)  # Output: Ali
# 💥 Destructor in Python:
# A destructor is a special method that is automatically called when an object is destroyed or goes out of memory.

# 📌 In Python, the destructor method is:

# def __del__(self):
# ✅ Purpose:
# To clean up resources like files, network connections, or memory before the object is removed.

# Rarely used, but useful in some advanced scenarios.

# 🔹 Example:

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} created")

#     def __del__(self):
#         print(f"{self.name} destroyed")

# s1 = Student("Ali")
# del s1  # Manually destroy the object (calls __del__ method)