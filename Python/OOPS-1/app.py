# OOPS(Object Oriented Programming System)
# To map with real world scenarios ,we started using objects in code .This is OOP


# Class and Object
# class is a blue-print for creating objects
# alone class cannot work with class we have to make an object also

# class
# class Student:
#     name = "aliqa"
#     age = 20
#     profession = "programmer"

# # object
# s1 = Student()
# print(s1.name) 
# ans aliqa
# print(s1)
# ans <__main__.Student object at 0x0000025B43E36A50>  [not the whole student class ]



# __init__ function or constructor
# ALL classes have a function called __init__()  which is always executed when a class/object is initiated


# class Student:
#   name = "aliqa"
#   def __init__(self): # self is a parameter which we have to pass we can also call it object bcz its the same thing
#    print(self) # if we print like this it will return "<__main__.Student object at 0x0000025B43E36A50>" which is also the location of our class
#    print("adding new name")

# __init__ is a default func which is created when an object or a class is executed it is not visible 
# we can add more parameters in __init__ func but the self is the first or mandatory
# "The self parameter is a refrence to the current insatance of the class , and is use to access variables that belongs to the class"


# s1 = Student()
# __init__ will be automatically called here 
# the ans will be "adding new name"


# it can also be written as:
# class Student:
#   def __init__(self, fullname, marks):
#     self.name = fullname
#     self.marks = marks

# s1 = Student("aliqa", 97) # we can also add more than one variable like s2=Student("ali")
# print(s1.name, s1.marks)
# ALL this is data or variables inside the object is called "ATTRIBUTES" in programming
# It is not compulsory to use classes nad object we can also save our data inform of list and dictionary or any other form but in future there will be such scenarios where we have to use classes and objects



# ATTRIBUTES
# there are two types of attributes
# 1. class [we can use for all the classes like name, age, hobby, etc]
# the things which we have common in all we make it class attributes
# 2. instance [depends upon objects]
# and those which are different we make it instance attributes

# class Student:
#    collge_name = "ABC College" [its class attribute]
#   def __init__(self, fullname, marks):
#     self.name = fullname [its an obj attribute bcz it will change witth every new student]
#     self.marks = marks


# if we have a class attrib or obj attrib of same name so always obj attrib will be the higher priority


# METHODS
# methods are functions tat belog to object

# class Student:
#    def __init__(self, fullname, marks):
#     self.name = fullname
#     self.marks = marks

#    def welcome(self): # its a method
#       print("Welcome Students, ", self.name)

#    def get_no(self): # its a method
#       return self.marks

# s1 = Student("aleem",97)
# s1.welcome()
# # ans  will be "Welcome Students"
# print(s1.get_no())
# ans  will be "Welcome Students,  aleem" and marks on second line "97"


# PRACTICE QS
# class Student:
#    def __init__(self, fullname, marks):
#     self.name = fullname
#     self.marks = marks

#    def average(self): 
#       sum = 0
#       for val in self.marks:
#         sum += val
#       print( "hi", self.name,"your avg score is", sum / 3)

# s1 = Student("kamil", [98, 71, 88])
# s1.average()
# ans will be hi kamil your avg score is 85.66666666666667

# if we want to change our attributes val
# s1.name = "faisal"
# s1.average()
# ans will be hi faisal your avg score is 85.66666666666667
   


# STATIC METHODS
# methods that dont use the self parameter [they work at class level]
# instead of self we use @staticmethod before writing static code and its called decorator
# "decorators allows us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it"
#  like
# class Student:
#     @staticmethod
#     def hello():
#         print("hello")

# Create an instance of the Student class
# s1 = Student()
# s1.hello()



# IMP CONCEPTS
# these are the pillars of OOPS
# ABSTRACTION: hiding the implementation details of the class and only showing the essential features to the user
# ENCAPSULATION: wrapping data and function into a single unit [object]


# abstraction is like all the code of class and object we dont show it on terminal only the imp part
# encapsulation is capsule of function and data which is object


# PRACTICE QS
# class Account:
#     def __init__(self, bal, acc):
#        self.balance = bal
#        self.account_no = acc
    
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.",amount , "was debited")
#         print("Total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.",amount , "was credited")
#         print("Total balance =", self.get_balance())


#     def get_balance(self):
#         return self.balance
        

# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(6000)