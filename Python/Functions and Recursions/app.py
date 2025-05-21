# FUNCTIONS
#  functions are used to perform specific tasks and can be reused throughout the code.
#  when we create a function it is not executed until we call it.
#  functions can take parameters and return values.

# def add(x, y): # inside the parantheses are the parameters of the function.
#     sum = x + y
#     print(sum) # this line will be executed when the function is called.
    # return sum  
    # print("This will not be printed") # this line will not be executed because it is after the return statement.

# add(5, 10) # calling the function with arguments 5 and 10. The function will return 15.

# if we want multiple line function in a single line we can use end=" " in print stat it will only give space 
# like
# print("Hello", end=" ")
# print("World") # this will print Hello World in a single line.



# there are two types of functions:
# 1. Built-in functions: these are functions that are already defined in Python and can be used directly.
#    Examples: print(), len(), type(), etc.
# 2. User-defined functions: these are functions that are defined by the user to perform specific tasks.
#    Examples: add(), subtract(), multiply(), etc.
#    User-defined functions can take parameters and return values.
#    User-defined functions can also have default parameters and keyword arguments.


# Types of functions arguments:

# 1. Positional Arguments
# Jo order mein diye jate hain.

# def greet(name, age):
#     print(f"{name} is {age} years old.")
# greet("Ali", 25)


# 2. Default Arguments
# Agar value na di jaye to default value use hoti hai.

# def greet(name="Guest"):
#     print(f"Hello, {name}!")
# greet()         # Hello, Guest!
# greet("Zara")   # Hello, Zara!


# 3. Keyword Arguments
# Explicitly variable ka naam dete ho.

# def student(name, grade):
# print(f"{name} got grade {grade}")
# student(grade='A', name='Ali')


# 4. Arbitrary Positional Arguments (*args)
# Jab exact number of arguments na pata ho.

# def total_marks(*marks):
#     return sum(marks)
# print(total_marks(75, 80, 90))  # Output: 245


# 5. Arbitrary Keyword Arguments (**kwargs)
# Jab unknown keyword arguments ho.

# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# student_info(name="Ali", age=20, course="AI")


# 1. Positional Arguments
# Definition:
# When we pass values to a function, the order of values matters. The first argument corresponds to the first parameter, the second to the second, and so on.

# Example:
# def add(a, b):
#     return a + b

# print(add(5, 10))  # a=5, b=10
# Important:
# The first value goes to the first parameter, the second value to the second, and so on.

# 🔥 2. Keyword Arguments
# Definition:
# We pass values to a function by specifying the name of the parameter. This way, the order doesn’t matter.

# Example:
# def add(a, b):
#     return a + b

# print(add(b=10, a=5))  # a=5, b=10
# Important:
# As long as you name the parameter, the order of values doesn't matter.

# 🔥 3. Default Arguments
# Definition:
# When a function has default values set for parameters, and if no argument is passed for that parameter, it uses the default value.

# Example:
# def greet(name="Guest"):
#     return "Hello " + name

# print(greet())           # Hello Guest
# print(greet("Amit"))     # Hello Amit

# Important:
# If no value is given for a parameter, the function uses the default value.
# If a value is provided, that is used instead.

# 🔥 4. Variable-Length Arguments
# Definition:

# When we don’t know how many arguments will be passed to the function, we use *args or **kwargs.

# 🔸 a) *args ➔ Positional Variable Arguments
# It collects extra positional arguments and stores them in a tuple.

# Example:
# def add(*numbers):
#     return sum(numbers)

# print(add(1, 2, 3, 4))  # 10
# 🔸 b) **kwargs ➔ Keyword Variable Arguments
# It collects extra keyword arguments and stores them in a dictionary.

# Example:
# def profile(**info):
#     print(info)

# profile(name="Amit", age=25)
# Output: {'name': 'Amit', 'age': 25}




# 🔸 Special Function Types

# 1. Lambda (Anonymous Function)
# Short one-liner functions.

# square = lambda x: x * x
# print(square(5))  # Output: 25


# 2. Recursive Function
# Jo khud ko hi call karta hai.

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  # Output: 120



# PRACTICE QUESTIONS


# num = [1, 2, 3, 4, 5, 6] 

# def print_list(num):
#   print(len(num))

# print_list(num)
# # this will print the length of the list num.

# def print_list(num):
#     for item in num:
#         print(item, end=" ") 

# print_list(num)
# this will print the list num in a single line.



# def fact(n):
#     factor = 1
#     for i in range(1, n+1):
#         factor *= i
#         print(factor)

   
# fact(n=5)
# this will print the factorial of 5 nums 

# def number(n):
#     if n%2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")


# num = int(input("Enter any number:"))
# number(num)


# ///////////////////////////////////////


# RECURSIONS
# when a function calls itself repeatedly
# recursion is another name of loops in a different way 
# we dont often use recursions only when its necessary

# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)
# # when we call function again in a function its calld recursive function

# show(6)


# def fact(n):
#     if (n == 0):
#         return 1
#     return(n-1) * n
# # in recursion we apply return twice
# print(fact(3))

# PRACTICE QS

# def sum(n):
#     if (n == 0):
#        return 0
#     return sum(n-1) + n
    
# print(sum(5))

# names = ["ali", "hassan", "hussain"]

# def one(list, i):
#     if (i == 0):
#         return 0
#     return i + 1
#     # OR
#     # return list/ list + 1

# print(names)
# it was partially right like it gave the right ans but wasnt called a recursive function in a right way

# THE Correct One
 
# def recurs_func(list, i = 0):
#     if(i == len(list)):
#      return
#     print(list[i])
#     recurs_func(list, i+1)


# names = ["ali", "hassan", "hussain"]

# recurs_func(names) 
    