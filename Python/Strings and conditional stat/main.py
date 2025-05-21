# string = "string",
# string = """string""",
# string = 'string'
#  we can use any of the above syntax to define a string 
#  but when we are using apostrophe in the string then we should use double quotes and vice versa
#  like
# str = "I'm a string"





# Escape sequence characters are :

# \n	New line (nayi line)	print("Hello\nWorld")	Hello
# World
# \t	Tab space	print("Hello\tWorld")	Hello World
# \'	Single quote	print('It\'s good')	It's good
# \"	Double quote	print("He said \"Hi\"")	He said "Hi"
# \\	Backslash	print("C:\\Drive")	C:\Drive
# \b	Backspace (1 char hatao)	print("Helloo\b")	Hello
# \r	Carriage return	print("12345\rabc")	abc45




# Concatenation of strings

# we dont use , in between strings to concatenate them
# len function is used to find the length of the string
# str1 = "Hello"
# str2 = "world"
# print(len(str1)) #5
# print(str1+str2) #Helloworld
# we can also put " " in b\w strings to add space in between code but it is also considered as a string
# like
# print(len(str1+" "+str2))
# the total length of helloworld is 10 but after adding space it will be 11





# Indexing in Strings

# str = "Hello"
# in languages index starts from 0 like here our h is on index 0 
# even special characters also bear an index no like
# str = "Hello_world"
# here our _ is on index 5
# there is also negative indexing like below but mostly we dont use it except slicing coz it is not considered as valid
# str = "Hello"
# here our o is on index -1 and so on
# we can only access the characters of string by using index no not change them 





# Slicing in Strings

# str = "hello"
# in slicing we can get a particular part of our string by using index no
# like
# print(str[0:3])
# it will print value from 0 index to 2 eg. hel
# if we want our last character so we can get it by 3 ways
# 1. print(str[0:5])  like this by adding +1 in the index no 
# 2. print(str[0:len(str)])  using len function it will also give u the same result e.g hello
# 3. print(str[0:])  server will auto take the last index no as the last index of the string and same with the starting index no
# like print(str[:5]) it will also give u the same result e.g hello
# we can also use negative indexing in slicing it also starts from -1
# like 
# print(str[-4:-1]) it will print the value from from -1 to -3 e.g it only works in python





#  Strings Function

#  sub-strings are short strings like "er" or a part of a string
# str = "i am a coder"

# print(str.endswith("er")) # if it is right it will give us a true if not it will give false

# print(str.capitalize()) # it will capitalize the first letter of our string it will work only once not in the main string
# str = str.capitalize() # this will change in the main string after printing

# print(str.replace("i am","You are")) # it replaces old value to new value

# print(str.find("a")) # here if we want to find some letter so it will provide us the index no of its first occurence
# like we have a 2 times in our string but it will provide us with index no if 1 a
# we can find words also
# if it doesnt exist so it will return -1
# eg : 2

# print(str.count("am")) # it will count the occurence of your given word or letter
# like we have "am" only once so it will give us 1





# Practice questions

# name = input("Enter your name:")
# print(len(name))

# string = "Hi $ i am $ sign and used in $ currency "
# print(string.find("$"))





#  Conditional Statements

# age = 20

# if (age >= 20):
#     print("You are an adult.")
# elif (age <= 18):
#     print("You are a teenager.")
# else:
#     print("You are a child.")  
# we can make as many if and elif if we want but we have to start from if
# the diff b\w them is that if prints the value if its true even if we have many if statements it will be printed until and unless its true
# but if we have if and elif statement and we have both true statements still we will only print the if value by default
# in python we use indentation which is proper spacing in js we use {} but in pyton we use indentation to write code and it holds great value

# marks = 90

# if (marks >= 90):
#     print("Grade A")
# elif (marks >= 80):
#     print("Grade B")
# elif (marks >= 70):
#     print("Grade C")
# elif (marks >= 60):
#     print("Grade D")
# else:
#     print("FAIL")





# Nesting statement

# it means when we create an if statement inside an if statement
# age = 18

# if (age >= 18):
#     if (age >= 80):
#         print("Cannot drive")
#     else:
#         print("Can drive")
# else:
#     print("Cannot drive")





# Practice Questions

# num = int(input("Enter a Number:"))

# if (num % 2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")

# a = 50
# b = 65
# c = 56
# d = 66

# if ( a > b and a > c and a > d):
#      print("A is the greatest of all")
# elif ( b > c and b > d):
#         print("B is the greatest of all")
# elif ( c > d):
#         print("C is the greatest of all")
# else:
#     print("D is the greatest of all")
    

# num = int(input("Enter a Number:"))

# if (num % 7 == 0):
#     print("The number is a multiple of 7")
# else:
#     print("The number is not a multiple of 7")