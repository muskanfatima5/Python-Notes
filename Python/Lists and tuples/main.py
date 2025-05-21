# LIST
# a built-in data type that stores a sets of items in a single variable
# like integer,float,string,bollean etc
# its a sort of an array but more flexible

# student = ["alice", 17, 94.2, True ]
# its a list of diff types but its type will be list
# strings are immutable/non-changeable whereas lists are mutable/can be changed
# like in str 
# name = "alice"
#  name[0] = "A" this will give an error
# but in list we can change the value

# list slicing
# same as string slicng last index is not included
# name = ["alice", "bob", "charlie", "danny", "edam", "frank"]
# print(name[0:3])
# so alice till charlie will be printed


# list Methods

# list = [1,2,3,4,5]
# list.append(6) 
# print(list)
# append means adding a value in the last
# so it will become this after printing [1, 2, 3, 4, 5, 6]


# list = [1,9,3,7,5]
# print(list.sort())# in this way it will give us a none ans and will sort thr list in next step like
# print(list)
# same goes for all methods u have to first apply the particular method in first step  then print in second step
# list.sort()
# print(list) whereas like this it will sort in this step
# it will automatically sort in ascending form like this [1, 3, 5, 7, 9]
# if we want sort in descending order we will print like this
# list.sort(reverse = True)
# print(list)
# the ans will be [9, 7, 5, 3, 1]
#  sort also works with strings but in alphabetic form like first string will be from 'a' second from 'b' and so on


# list=["a", "b", "c", "d"]
# list.reverse()
# print(list)
# the ans will be ['d', 'c', 'b', 'a']


# list = [1,2,3,4,5]
# list.insert(5,6)
# print(list) ans will be [1, 2, 3, 4, 5, 6]
# list = ["apple", "banana", "orange"]
# list.insert(2, "kiwi")
# print(list) ans will be ['apple', 'banana', 'kiwi', 'orange']

# list = [1,2,3,4,5.1]
# # list.remove(1)
# # print(list) it only removes the first occurence of an element
# list.pop(4)# write index no of the value we want to be removed
# print(list)[1, 2, 3, 4]



# TUPLES
# a built-in data type that lets us create immutable sequences of values
# as in list we can change their values but in tuples we cannot
# the diff b/w tuples and list is parenthesis in lists we use square brackets whereas in tuple we use paranthesis
# slicing is same as in lists
# name = (1, "alice", 2, 3, "ally")
# print(type(name))

# for single item tuple "," is imp
# num = (1) ans 1
# num = (1,) ans (1,)
# print(num)

# tuples Method

# num = (1, 2, 3, 4, 1, 2)
# print(num.index(2))
# only gives u the index no of occurence of an element


# num = (1, 2, 3, 4, 1, 2)
# print(num.count(2))
# gives us the count of an element



# Practice Questions
# movies = []
# mov1 = (input("Enter your favourite movie name: "))
# mov2 = (input("Enter your favourite movie name: "))
# mov3 = (input("Enter your favourite movie name: "))

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print (movies)



# palinddrome means a  word which after reversing pronounced as same
# like ma'am, racecar or eve 

# name = [1, 2, 3, 2, 1]
# name2 = [1,2,3]
# name3 = ["r","a","c","e","c","a","r"]

# copy = name3.copy()
# copy.reverse()

# if (copy == name3 ):
#    print("Palindrome")
# else:
#    print("Not Palindrome")


# grade = ["C","A","B","D","A","C","A"]
# # print(grade.count("A"))
# grade.sort()
# print(grade)


# Feature	    List	          Tuple	     Dictionary
# Ordered?	    ✅ Yes	        ✅ Yes	  ❌ No (Python 3.6+: Insertion order kept)
# Mutable?	    ✅ Yes	        ❌ No	  ✅ Yes
# Index-based?	✅ Yes	        ✅ Yes	  ❌ No (key-based)
# Hashable?	    ❌ No	        ✅ Yes	  ✅ Keys must be hashable
# Syntax	    [ ]	             ( )	     { key: value }
# Use	     Changeable list	Fixed data	Fast lookup via key



# Hashable – Jiska taala kholne ka ek fix chabi number hota hai (hash value)
# Yeh woh objects hote hain jinka:

# hash value fix hota hai (hash(obj) chalega)

# Wo object kabhi badalta nahi (immutable)

# Isliye, Python dictionaries ke keys ya sets ke elements ban sakte hain

# Examples of hashable types:

# int, float, str

# tuple (only if it contains hashable elements)

# bool

# frozenset


# Unhashable – Jiska taala kholne ke liye chabi har baar badalti hai (no fixed hash)
# Yeh woh objects hote hain jo:

# badal sakte hain (mutable)

# Isliye unki hash value consistent nahi hoti

# Python unko dictionary ke keys ya set ke element mein nahi lene deta

# 📌 Examples of unhashable types:

# list

# dict

# set


# 🔢 Data Type	🔄 Mutable?	    📌 Notes
# int	         ❌ Immutable	Integer (e.g. 1, 42)
# float	         ❌ Immutable	Decimal (e.g. 3.14)
# bool	         ❌ Immutable	True / False
# complex	     ❌ Immutable	Complex numbers (e.g. 2 + 3j)
# str	         ❌ Immutable	Strings (e.g. "hello")
# tuple	         ❌ Immutable	Fixed-size sequence
# frozenset	     ❌ Immutable	Immutable version of set
# bytes	         ❌ Immutable	Immutable binary data
# range	         ❌ Immutable	Range object (e.g. range(5))

# 📦 Collection Type	🔄 Mutable?	  📌Notes
# list	                 ✅ Mutable	 Change, add, remove items
# set	                 ✅ Mutable	 Unordered, unique items
# dict	                 ✅ Mutable	 Key-value pairs
# bytearray	             ✅ Mutable	 Mutable version of bytes
# collections.deque	     ✅ Mutable	 Fast appends/pops from both ends