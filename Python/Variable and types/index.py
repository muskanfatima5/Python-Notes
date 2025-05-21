# python was developed by Guido van Rossum in 1991
# python is a very simple and easy language
# implicit means auto change or whatever and explicit means we have to do it

# print("Hello World!")

# variables
# name = "muskan"
# age = 20
# hobby = "reading"

# print("My name is", name)
# print("My age is", age)
# print("My hobby is", hobby)
# = is assignment operator

# In python we can assign one variables as a value of another variable 
# like
# hobby2 = hobby
# print("I like", hobby2)
# In python variables can be a combination of upper nad lower case letters, underscores or digits
# but they cant start with a digit

# Data types
# integer ,float, string, boolean, none
# float is a number with a decimal point
# boolean only works with True or False with only first letter capital none also works with first letter capital

# a = 10
# b = 5
# sum = a + b
# print(sum)
# sum is the additional value
# diff = a - b
# print(diff)
# diff is the subtraction value

# Operators

# Arithmetic operators
# +, -, *, /, %, **, //

# Comparison operators
# ==, !=, >, <, >=, <=

# Assignment operators
# =, +=, -=, *=, /=, %=, **=, //=  

# Logical operators
# and, or, not


# print (a - b)
# print (a + b)
# print (a * b)
# print (a / b)
# print (b % a)
# print (a ** b) 
#  means power  like 10 isto power 5 = 100000
# print (a // b)
# print (a / b)
# means floor division like 10 divided by 5 = 2
# only diff is // is floor division and / is normal division 
# floor divisions answer is always an integer
# normal divisions answer is always a float

# a = 10
# b = 5
# print (a == b) 
# print (a != b)
# print (a > b)
# print (a < b)
# print (a >= b)
# print (a <= b)
# false, true, true, false, true, false

# a = 10
# b = 5

# a += b
# print(a)
# 15
# a -= b
# print(a)
# 5
# a *= b
# print(a)
# 50
# a /= b
# print(a)
# 2.0
# a %= b
# print(a)
# 0
# a **= b
# print(a)
# 100000
# b //= a
# print(b)
# 0


# print ( not a == b)
# not navigates the answer in negative form

# print (a != b and a > b)
# and operator works only answers true when both the conditions are true

# print (a != b or a < b)
# or operator can answer true even if only one condition is true

# Type conversion or Type casting
# conversion is auto or casting is manual 

# a = 4.75
# b = 6.25
# print (a + b)
# it will give an ans 11.0

# a = 4
# b = 6.25
# print (a + b)
# whereas it will give a ans of 10.25

# a = "4"
# b = 6
# print (a + b)
#  it will give an error

# means In type conversion we can convert integer to float but not float to integer or string to integer or float
# whereas in type casting we can convert float to integer or integer to float or string to integer or float
# like
# a = "4"
# b = 6.25
# print (b + int(a))
# ans 10.25

# a = "4.75"
# b = 6.25
# print (b + float(a))
# ans 11.0

# a = 4.75
# b = 6.25
# print (int(b) + int(a))
# ans 10

# a = 4
# b = 6
# print (float(b) + a)
# ans 10.0

# but we cannot mix string with float or int
# like 
# a = "abc"
# b = 6.25
# print (b + int(a))
# it will give an error

# Input 

# name = input("Enter your name:")
# print("Hello", name)
# input is always a string
# age = input("Enter your age:")
# print(type(age), age )
# type will show str even if we enter an int
# if we wnat input in int we have to type cast it 
# like
# age = int(input("Enter your age:"))
# print(type(age), age )
# now it will show the type as int 

# val1 = int(input("Enter first number:"))
# val2 = int(input("Enter second number:"))
# sum = val1 + val2
# print("The sum is", sum)

# val1 = float(input("Enter first number:"))
# val2 = float(input("Enter second number:"))
# sum = val1 + val2 
# print("The sum is", sum / 2)

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:")) 
# print(a > b)