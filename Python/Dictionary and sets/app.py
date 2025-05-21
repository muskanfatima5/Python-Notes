# DICTIONARY
# used to store data values in keys:value pairs
# they are mutable, unordered and dont allow duplicate keys
# info = {
#     "name" : "ally",
#     "age" : 21,
#     "hobby" : "reading"
# }
# print(info)

# Nested dictionary
# info = {
#     "name" : "ally",
#     "age" : 21,
#     "hobby" : "reading",
#     "subjects" : {
#         "physics" : 78,
#         "english" : 89,
#         "bio" : 85,
#         "chem" : 82
#     }
# }
# print(info["subjects"]["physics"])

# Dictionary Methods

# print(list(info.keys()))returns all keys as a list
# print(len(list(info.keys())))returns the length of dictionary

# print(info.values()) returns all values of keys

# print(info.items())returns all key/values as tuple in pairs
# pairs = list(info.items())
# print(pairs[1]) if we want a particular pairs

# print(info["name1"]) 
# but if we write name1 which is wrong so the above will provide error whereas the below .get will provide none
# print(info.get("name1"))

# info.update({"city": "karachi"})
# print(info) add a new item to the dict

# how to create an empty dictionary
# case = {}
# print(type(case))

# how to add in empty dictionary
# subjects = {}
# subjects.update({"english" : 91})
# subjects.update({"math" : 90})
# subjects.update({"bio": 85})
# OR
# subjects = {}
# subjects["english"] = 91
# subjects["math"] = 90
# subjects["bio"] = 85
# print(subjects)




# SETS
# collection of the unordered items, each element in the set must be unique and immutable but sets are mutable 
# cannot be changed or one element can appear once only not more than one

# collection = {1, 2, 3 , 4, 5, 1}
# print(collection)the ans will be {1, 2, 3, 4, 5}
# value = { "abc", "bcd", "cda", "abc", "bca"}
# print(value) the ans will be {'bcd', 'bca', 'cda', 'abc'}
# print(type(collection))

# how to create an empty set
# case = set()
# print(type(case))


# Set Methods


# copies = set()
# copies.add(1) # can add only one element at a time
# copies.add(2)
# copies.add(13)
# copies.add(3)
# print(copies)
# copies.remove(13)
# print(copies)
# print(copies.pop()) picks up a random value: ans 1

# copies.clear()
# print(copies)
# we can add a tuple or string or integer but not list or dict coz it can be changeable

# set1 = {1,2,3,4,5}
# set2 = {5,6,7,8}
# # print(set1.union(set2)) ans {1, 2, 3, 4, 5, 6, 7, 8}
# print(set1.intersection(set2)) ans {5}



# Frozen SET
#  A frozenset is just like a set (a collection of unique, unordered elements), 
# but it's immutable — meaning you can’t change it after it's created.
# You can use it as a dictionary key (since it's hashable).
# You can’t add or remove items from it

# Creating a frozenset from a list
# my_list = [1, 2, 3, 2, 1]
# fs = frozenset(my_list)

# print("Frozenset:", fs)  # Output: frozenset({1, 2, 3})

# Trying to add an item (this will cause an error)
# fs.add(4)  # ❌ Error: 'frozenset' object has no attribute 'add'

# Using frozenset in a set or as a dictionary key
# fs = frozenset([1, 2, 3])  # Define fs as a frozenset
# my_dict = {fs: "frozen"}
# print("Dictionary using frozenset as key:", my_dict)

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])

# print("Union:", a | b)           # {1, 2, 3, 4, 5}
# print("Intersection:", a & b)    # {3}
# print("Difference:", a - b)      # {1, 2}


# Feature	frozenset
# Mutable?	❌ No
# Duplicates?	❌ No
# Ordered?	❌ No
# Hashable?	✅ Yes
# Useful for	Set operations, keys in dictionaries


# Hashable examples
# x = 10
# print(hash(x))         # ✅ Works! Integers are hashable

# s = "hello"
# print(hash(s))         # ✅ Strings are hashable

# t = (1, 2, 3)
# print(hash(t))         # ✅ Tuples are hashable (if they contain only hashable items)

# Unhashable example
# l = [1, 2, 3]
# print(hash(l))       # ❌ Error: lists are not hashable because they can change



# PRACTICE QUESTIONS

# thing = {
#     "name" : "table",
#     "means" : ["a piece of furniture","a list of facts and figures"],
#     "name2" : "cat",
#     "means2": "a small animal",
#     }
# print(thing)

# lang = {
#     "python", "Java", "C++", "python", "Javascript", "Java", "python", "Java","C++","C"
# }
# print(len(lang))

# subjects = {}
# subjects.update({"english" : 91})
# subjects.update({"math" : 90})
# subjects.update({"bio": 85})
# # subjects["english"] = 91
# # subjects["math"] = 90
# # subjects["bio"] = 85
# print(subjects)

# value = {9 , 9.0}
# print(value)ans {9} bcz python considers 9 or 9.0 as same if we want to print both then we can use string once like "9.0" 
# or we can add it in tuple form in a set
# value = {
#     ("float", 9.0),
#     ( "int", 9)
# }
# print(value)