# Hashable = “unchangeable + has a unique ID number”

# Del keyword in objects
# used to delete object properties or objects itself
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("fati")
# print(s1)
# del s1
# print(s1)
# give an error

# PRIVATE attributes and methods
# conceptual implementations in python
# Private attributes and methods are meant to be used only wuthin the class and are not accessible from outside the class
# the attributes those are private like password or any other which we dont want to share so will private it by adding __ before 
# it will not work outside the class but can work fine inside the class
# like
# class Student:
#     def __init__(self, name, id):
#         self.name = name
#         self.__id = id

#     def reset_id(self):
#         print(self.__id)

# s1 = Student("fati", 12345)
# print(s1.reset_id())
# it will give us an ans 12345 and "None" on next line
# print(s1._id)
# it will give us error


# Inheritance [third pillar of OOPS]
# when one class[child/derived] derives the properties and methods of another class[parent/base] 

# class Car:
    
#     def start(self):
#         print("car start..")
#     @staticmethod
#     def stop():
#         print("car stoping..")

# class Toyotacar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = Toyotacar("Fortuner")
# car2 = Toyotacar("Prius")

# print(car1.start())
# this is a single inheritance type a single parent and a child class

# Types of inheritance
# Single 
# Multi-level
# Multiple

# class Car:  
#     def start(self):
#         print("car start..")
#     @staticmethod
#     def stop():
#         print("car stoping..")

# class Toyotacar(Car):
#     def __init__(self, brand):
#         self.brand = brand


# class Fortuner(Toyotacar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()
# this is an example of multi-level inheritance


# class Car:  
#     def start(self):
#         print("car start..")
#     @staticmethod
#     def stop():
#         print("car stoping..")

# class Toyotacar:
#         brand = "Toyota brand"



# class Fortuner(Car, Toyotacar):
#     def __init__(self, type):
#         self.type = type
        

# car1 = Fortuner("Diesel")
# print(car1.start())
# print(car1.brand)
# print(car1.type)
# this is an example of multiple inheritance



# SUPER Method
# super() method is used to access methods of the parent class [super means parent in inheritance]

# class Car:  
#     def __init__(self, type):
#         self.type = type
         
#     def start(self):
#         print("car start..")
#     @staticmethod
#     def stop():
#         print("car stoping..")

# class Toyotacar(Car):
#     def __init__(self, brand, type):
#         super().__init__(type)
#         self.brand = brand

# car1 = Toyotacar("Prius", "electric")
# print(car1.type)


# CLASS Method
# a class method is bound to the class and recieves the class as an implicit first argument
# Note-static method cant access or modify class state and generally for utility


# class Person:
#     name = "anonymous"

    # def changename(self, name):
    #     Person.name = name

# p1 = Person()
# p1.changename("ariz")
# print(p1.name)
# print(Person.name)

        # OR

#     def changename(self, name):
#         self.__class__.name = "YAHYA"

# p1 = Person()
# p1.changename("ariz")
# print(p1.name)
# this is how we can normally change our name attribute in a class from outside



# this is how we change inside the class [below]
# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls, name):
#      cls.name = name

# p1 = Person()
# p1.changeName("ariz")
# print(p1.name)


# PROPERTY
# we use @property decorator as a method in the class to use the method as a property

# class Student:

#     def __init__(self, phy, chem, bio):
#         self.phy = phy
#         self.chem = chem
#         self.bio = bio 
#         self.percentage = str((self.phy + self.chem + self.bio) / 3) + "%"

#     def calPercent(self):
#         self.percentage = str((self.phy + self.chem + self.bio) / 3) + "%"

# stu1 = Student(98, 94, 91)
# print(stu1.percentage)
# now if we want to change any of the subj marks we will add function of calPercent and below code

# stu1.phy = 90
# print(stu1.phy)
# stu1.calPercent()
# print(stu1.percentage)

# but with [property method] we can code like this

# class Student:

#     def __init__(self, phy, chem, bio):
#         self.phy = phy
#         self.chem = chem
#         self.bio = bio 
    
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.bio) / 3) + "%"

# stu1 = Student(98, 94, 91)
# print(stu1.percentage)

# stu1.phy = 90
# print(stu1.percentage)



# POLYMORPHISM 
# its the fpourth pillar of OOPS
# when the same operator is allowed to have different meaning according to the context

# Dunders Functions
# basically we use dunder functions in complex nos
# we can goto docs.python documentation for further details
# a + b [addition] a.__add__(b)
# a - b [subtraction] a.__sub__(b)
# a * b [multiplication] a.__mul__(b)
# a / b [division] a.__truediv__(b)
# a % b [modulus] a.__mod__(b)

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +",self.img,"j")

# n1 = Complex(4 ,10)
# n1.showNumber()



# how to use dunder functions
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +",self.img,"j")

#     def add(self, n2):
#         newReal = self.real + n2.real
#         newImg = self.img + n2.img
#         return Complex(newReal, newImg)


# n1 = Complex(4 ,10)
# n1.showNumber()

# n2 = Complex(10 ,2)
# n2.showNumber()

# n3 = n1.add(n2)
# n3.showNumber()
# this is the simple way to add


# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +",self.img,"j")

#     def __add__(self, n2):
#         newReal = self.real + n2.real
#         newImg = self.img + n2.img
#         return Complex(newReal, newImg)


# n1 = Complex(4 ,10)
# n1.showNumber()

# n2 = Complex(10 ,2)
# n2.showNumber()

# n3 = n1 + n2
# n3.showNumber()
# this is how we do by using dunder func


        
# PRACTICE QS
# class circle:
#     def __init__(self, radius):
#        self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def parameter(self):
#         return 2 * (22/7) * self.radius
    

# c1 = circle(21)
# print(c1.area())
# print(c1.parameter())


# class Employe:
#     def __init__(self, role, department, salary):
#        self.role = role
#        self.department = department
#        self.salary = salary

#     def showDetails(self):
#         print(self.role, self.department, self.salary)
    

# empl = Employe("intern", "Information Technology", 60000)
# # print(empl.role, empl.department, empl.salary)
# print(empl.showDetails())
# its for when we have only employe class

# class Engineer(Employe):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","76000")


# engin = Engineer("Ali", 26)
# engin.showDetails()


# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, ord2):
#         return self.price > ord2.price


# ord1 = Order("chips", 100)
# ord2 = Order("cake", 60)

# print(ord1 > ord2)