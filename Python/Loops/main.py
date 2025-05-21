# LOOPS
# loops are used to repeat a block of code multiple times
# there are two types of loops in python
# 1. for loop
# 2. while loop
# in loops variables are also called iterators and looping is called iteration like 1 loop neabs 1 iteration


# WHILE loop

# count = 2
# while count <= 5:
#     print("hello") if we write till here so it will print hello infinite times thats why last step is imp 
#     count += 1


# PRACTICE QUESTIONS

# num = 1
# while num <= 100:
#     print(num)
#     num += 1

# num = 100
# while num >= 1:
#     print(nump
#     num -= 1

# num = 3
# while num <= 30:
#     print(num)
#     num += 3
# OR
# i = 1
# while i <= 10:
#     print(i * 3)
#     i += 1
# this way we can print table of any no by replacing 3 with any no
 

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# x = 25

# i = 0
# while i < len(num):
#     if (num[i] == x):
#         print("Found at index", i)
#     i += 1

# /////////////////////////////////////////


# loops also have break and continue statements

# break stat is used to exit the loop or to stop the loop
# for example if we want to print 1 to 10 but stop at 5 so we can use break statement
# i = 1
# while i <= 10:
#     if i == 6:
#         break
#     print(i)
#     i += 1
# ans will be 1 2 3 4 5



# continue stat is used to skip the current iteration and continue with next iteration
# for example if we want to print 1 to 10 but skip 5 so we can use continue statement
# i = 1
# while i <= 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1
# ans will be 1 2 3 4 6 7 8 9 10



# FOR loop
# for loop is used for sequencial traversal of a sequence [sequencial traversal means to go through each element of a sequence one by one]
# for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string)
# like

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# for eat in fruits:
#     print(eat)
# ans will be 
# apple
# banana
# cherry
# kiwi
# mango


# name = "alexander white garrid"
# for char in name:
#     print(char)
# ans will be
# a
# l
# e
# x
# a
# n
# d
# e
# r

# w
# h
# i
# t
# e

# g
# a
# r
# r
# i
# d

# we can use else also with loops
# else statement is executed when the loop is finished
# for example if we want to print 1 to 10 and then print "done" when the loop is finished so we can use else statement


# PRACTICE QUESTIONS


# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 25

# # for i in num:
# #     print(i)

# for i in num:
#     if i == x:
#         print("Found at index", num.index(i))
#         i += 1
#  the above search is called linear search

# ///////////////////////////////////////////////


# RANGE Function
# range is used to generate a sequence of numbers
# range(start, stop, step)

# for i in range(0, 11, 2): # (start, stop, step means increment by 2 )
#     print(i) # ans will be 0 2 4 6 8 10

# PRACTICE QUESTIONS

# for i in range(1, 101):
#      print(i)
# ans will be from 1 to 100


# for i in range(100, 0, -1):
#      print(i)
# ans will be from 100 to 1


# for i in range(0,  51 , 5):
#    print(i)
# OR
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#    print(i * n)
# if we want any table

# /////////////////////////////////////////


# PASS statement
# pass statement is used to do nothing it is not frequently used in python
# it is used when we want to do nothing in a loop or function or class
# for example if we want to create a function but we dont want to write anything in it so we can use pass statement
# it is used as a placeholder for future code like if we want to write code later but we dont want to write anything now so we can use pass statement

# for i in range(5):
#   pass # this will do nothing
# print("Hello") # this will print Hello


# PRACTICE QUESTIONS

# n = 5

# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1
# OR


# for i in range(1, n + 1):
#     sum += i

# print("Sum of first", n, "natural numbers is", sum) # works for both while and for loop
# ans will be 15



# n = 5
# sum = 1
# i = 1

# for i in range(1, n + 1):
#     sum *= i
#     print(sum)

# while i <= n:
#     sum *= i
#     i += 1
#     print("the toal is", sum)