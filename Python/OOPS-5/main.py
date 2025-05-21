# STATIC METHODS, COMPOSITION, AGGREGATION, MRO(Method Resolution Order) AND DIAMOND INHERITANCE, OVERRIDE, FUNCTION DECORATORS, CLASS DECORATORS


# What is a Static Method?
# A static method is a method that behaves like a regular function but is defined inside a class for organizational purposes. It is declared using the @staticmethod decorator.

# 🔸 Syntax:

# class MyClass:
#     @staticmethod
#     def my_static_method(arg1, arg2):
#         # does not use self or cls
#         return arg1 + arg2
    

# 🔹 Key Points:
# Defined using @staticmethod.
# Does not take self or cls as the first parameter.
# Can be called using the class name or an object of the class.
# Typically used for utility functions related to the class but that don’t need access to class or instance data.

# 🔸 Example:

# class Calculator:
#     @staticmethod
#     def add(x, y):
#         return x + y

# # Calling static method
# print(Calculator.add(5, 3))       # Output: 8

# # Also callable via object
# calc = Calculator()
# print(calc.add(10, 2))            # Output: 12


# 🔹 When to Use Static Methods:
# When the method performs a generic operation related to the class.
# When you don’t need to access or modify instance/class attributes.
# For helper or utility methods.


# 🧱 What is Composition in OOP (Object-Oriented Programming)?
# Composition is an OOP concept where one class contains an object of another class as a part of its state. It allows you to build complex types by combining objects of other types, similar to a “has-a” relationship.

# 🔹 Real-Life Analogy:
# A Car has an Engine.
# So instead of Car inheriting from Engine, we say:
# Car uses or contains an Engine object inside it — this is composition.

# 🔸 Syntax Example in Python:

# class Engine:
#     def start(self):
#         print("Engine started")

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Composition: Car has an Engine

#     def start(self):
#         self.engine.start()
#         print("Car is ready to go!")

# # Usage
# my_car = Car()
# my_car.start()

# 🔹 Output:
# Engine started
# Car is ready to go!


# 🧩 What is Aggregation in OOP?
# Aggregation is a "has-a" relationship like composition, but with one key difference:
# 🔹 In aggregation, the contained object can exist independently of the container class.
# 🔸 In Simple Words:
# Composition: Strong ownership — if the container is destroyed, the part is destroyed.
# Aggregation: Weak ownership — if the container is destroyed, the part can still exist.

# 🔹 Real-Life Example:
# Class	     Relationship	                    Can Exist Independently?
# Department → Teacher  A Department has Teachers	✅ Yes, a Teacher can exist without a Department
# Car        → Engine	A Car has an Engine	        ❌ No, the Engine is tightly bound to the Car

# 🔸 Example in Python:

# class Teacher:
#     def __init__(self, name):
#         self.name = name

# class Department:
#     def __init__(self, teachers):
#         self.teachers = teachers  # Aggregation: list of external Teacher objects

#     def show_teachers(self):
#         for teacher in self.teachers:
#             print(f"Teacher: {teacher.name}")

# # Teachers created independently
# t1 = Teacher("Alice")
# t2 = Teacher("Bob")

# # Aggregated into a department
# dept = Department([t1, t2])

# dept.show_teachers()
# 🖨️ Output:

# Teacher: Alice
# Teacher: Bob


# 🔸 Key Differences: Composition vs Aggregation
# Feature   	        Composition 	        Aggregation
# Type	            Strong "has-a"	        Weak "has-a"
# Object Lifecycle	Part dies with whole	Part can live independently
# Ownership	        Strong	                Loose
# Example  	        Car has Engine	        Department has Teachers



# 🧠 What is MRO (Method Resolution Order)?
# MRO is the order in which Python looks for methods or attributes when you call them from an object — especially when multiple inheritance is involved.

# 🔍 In Simple Words:
# If a class inherits from multiple classes, and those parent classes have the same method, Python needs to decide which one to run.
# The MRO decides that order.

# 🧪 Example:

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):  # Multiple Inheritance
#     pass

# d = D()
# d.show()


# 🤔 Which method will be called?
# We have:
# D inherits from B and C
# Both B and C have show() method

# ➡️ Python will follow MRO and call the first method it finds.

# print(D.__mro__)  # Shows the MRO order

# 🖨️ Output:
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# ✅ So it will call:
# B



# 💎 What is Diamond Inheritance?
# 🔸 Diamond inheritance happens when:
# A class inherits from two classes that both inherit from the same parent.

# 📐 Looks like a diamond:


#      A
#     / \
#    B   C
#     \ /
#      D
# 🔍 Problem:
# If all classes have the same method, and we create an object of D, which method should be called?

# 🧪 Example:

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):  # Diamond shape
#     pass

# d = D()
# d.show()
# 👉 Output:

# B
# Because Python’s MRO follows C3 Linearization, it goes left to right in inheritance:
# D → B → C → A → object

# 🧠 In One Line:
# MRO = Python’s way of deciding which method to call first when multiple parents have the same method.
# Diamond Inheritance = A situation where MRO is especially important because of overlapping parent classes.

# ✅ Quick Tip:
# You can always check the MRO using:

# print(YourClass.__mro__)
# # or
# help(YourClass)



# What is Method Overriding?
# ✅ Definition:
# Overriding means:
# A child class provides its own version of a method that is already defined in its parent class.

# Method Overriding
# Method overriding occurs when a subclass provides a specific implementation of a method that is 
# already defined in its superclass. The subclass method overrides the superclass method.

# 🧠 In Simple Words:
# Child rewrites the method of the parent using the same method name.

# 🧪 Example:

# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def greet(self):  # Overrides the parent method
#         print("Hello from Child")

# c = Child()
# c.greet()

# 🖨️ Output:
# Hello from Child
# 🔸 The child’s method overrides the parent’s version.

# 🎯 Why Use Overriding?
# To customize or extend the behavior of the parent class.

# Same method name, new behavior.


# 🎁 2. What are Function Decorators?
# ✅ Definition:
# A function decorator is a wrapper function that adds extra functionality to another function without changing its code.

# 🧠 In Simple Words:
# It's like putting a gift wrapper around a function to enhance it, like adding logging, timing, security, etc.

# 🧪 Example:

# def my_decorator(func):
#     def wrapper():
#         print("Something before the function runs")
#         func()
#         print("Something after the function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# 🖨️ Output:
# Something before the function runs
# Hello!
# Something after the function runs
# 🛠️ Where Are Decorators Used in OOP?
# In classes, we commonly use:

# Decorator	    Purpose
# @staticmethod	Defines a static method (no self)
# @classmethod	Method that receives cls instead of self
# @property	    Makes a method behave like an attribute




# 🧠 What is a Class Decorator?
# ✅ Definition:
# A class decorator is a special function that modifies or enhances a class when the class is defined — just like function decorators but for classes.

# 🔁 Think of it like putting a gift wrap around a class to change or add extra behavior without modifying the class code directly.

# ✅ Syntax:

# @decorator_function
# class MyClass:
#     ...
# 🧪 Simple Example:

# def add_info(cls):
#     cls.info = "This is a decorated class"
#     return cls

# @add_info
# class Person:
#     def __init__(self, name):
#         self.name = name

# p = Person("Amit")
# print(p.name)         # Output: Amit
# print(Person.info)    # Output: This is a decorated class

# 🧠 What happened here?
# @add_info is a class decorator.
# It added an extra attribute info to the class Person at the time the class was created.

# 🔧 When to Use Class Decorators?
# To add logging, metadata, or custom behavior.
# To register classes (common in plugin systems).
# To validate or modify class attributes.

# 🎯 Real-World Use Case Example:

# def register_class(cls):
#     print(f"Registering class: {cls.__name__}")
#     return cls

# @register_class
# class Order:
#     def __init__(self, id):
#         self.id = id
# 🖨️ Output:
# Registering class: Order
# ➡️ This is useful when you want to automatically log or track class creation.

# 🧠 Summary:
# Concept   	 Function Decorator	                Class Decorator
# Applied To	 Functions or methods	            Classes
# Purpose	     Modify function behavior	        Modify class behavior or structure
# Syntax	     @decorator_name above a function	@decorator_name above a class