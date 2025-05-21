# FILE INPUT/OUTPUT
# python can be used to perform operations in a file (read/write)

# Types of all Files:
# Text Files: .txt, .docx, .log, etc
# Binary Files: .mp4, .mov, .jpg, .png, .jpeg, etc

# Open, read and close file

# f = open("file.name","mode")
# data = f.read()
# f.close()

# f = open("demo.txt","rt")# "rt" or only "r" works as same
# # if we didnt have our file stored in the same folder so we have to write whole path in place of file name
# data =f.read()
# print(data) 
# print(type(data))
# f.close()
# its the sign of a good programmer to close a file after working

# "r" open for reading(default)
# "w" open for writing,truncating the file first(truncating means overwrite like if we want to write something in afile so the previous data will be deleted)
# "x" create a new file and open it for writing
# "a" open for writing, appending to the end of thefile if it exists
# "b" binary mode
# "t" text mode(default)
# "+" open a disk file for updating(reading and writing)


# f = open("demo.txt","rt")
# data =f.read(5)# if we want starting particular data
# print(data) 
# f.close()
# returns "I am "

# f = open("demo.txt","rt")
# data =f.readline()# if we want to read line by line
# print(data) 
# f.close()
# returns "I am learning" only first line
# in readline it returns the line then a line gap below it coz by default there is a textline so it will give us a gap there if there is text line below that particular line

# f = open("demo.txt","rt")
# line1 =f.readline()# we can also write it like this
# print(line1) 
# returns "I am learning" with a next line gap


# line2 =f.readline()
# print(line2) 
# f.close()
# returns "Programming Language" with a next line gap

# if we have already read the file and the we are reading it again line by line so it will return blank space in that those line not the text




# f = open("demo.txt", "a")
# f.write("this is a new line")# it will be added in your file
# f.close()
# I am learning 
# Programming Language
# Python
# from ApnaCollegethis is a new line
# if we want to write on new line then we will start with \n


# f = open("demo.txt", "w")
# f.write("I want to learn typescript")# this will be overwritten in your file after deleting the previous work
# f.close()
# I want to learn typescript


# if we ont have a file we have named in the open function then the default will create it by itself
# like
# f = open("sample.txt", "w")
# f.close()
# a new is created by default

# Stackoverflow article for further explanation

# if we want to read and write simultaneously then we will write "r+"
# 
# f = open("demo.txt", "r+")
# f.write("\n programmer")
# f.close()
# f = open("demo.txt", "r+")
# f.write("\n java")
# f.close()
# it will overwrite from the starting like
# previous code
#  "script"
#  presenet code "javapt" it overwrite from the start means replaces "scri" to "java"
#  No truncate


# f = open("demo.txt", "w+")
# f.write("\n script")
# f.close()
# "+w" will write after deleting previous data
#  truncate


# f = open("demo.txt", "a+")
# f.write("\n script")
# f.close()
# "a+" will overwrite at the end of code like
# previous code
# "java"
# present code "java" then "script" on next line
#  No truncate


# SYNTAX
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# previous code "This is a demo file for practice"
# present code in terminal "This is a demo file for practice"
# closing function is not compulsory for syntax coz it auto closes it


# Module {like a code library} is a file written by another programmer that generally has a function we can use

# import os
# os.remove("sample.txt")


# PRACTICE QUESTIONS

# f = open("sample.txt", "w")
# f.write("Hi everyone! we are learning File I/O using Java. \n I like programming in Java") 
# f.close()

# with open("sample.txt", "r")as f:
#     data = f.read()

# new_data =data.replace("Java","Python")
# print(new_data)

# with open("sample.txt", "w")as f:
#     data = f.write(new_data)
# when we want to replace the particular 


# with open("sample.txt", "r")as f:
#     data = f.read()
#     if (data.find("learning") != -1):
#         print("Found")
#     else:
#         print("Not Found")
# when we want to found a particular word

# OR we can write it as a function 

# def check_word():
#     with open("sample.txt", "r")as f:
#       data = f.read()
#       if (data.find("learning") != -1):
#         print("Found")
#       else:
#         print("Not Found")


# check_word()

# def check_line():
#     data = True
#     line_no = 1
#     with open("sample.txt", "r")as f:
#       while data:
#         data = f.readline()
#         if ("slearning" in data):
#          print(line_no)
#         line_no += 1

#     return -1

# print(check_line())
# when we want to find that particular words line no


# count = 0
# with open("demo.txt", "r")as f:
#    data = f.read()
   
# nums = data.split(",")
# for val in nums:
#     if(int(val) %2 == 0):
#         count += 1 

# print(count)
# when we want to count the len of even no