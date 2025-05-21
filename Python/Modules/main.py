# 1. Module kya hota hai?
# Module ek Python ka file (.py) hota hai jisme kuch code likha hota hai – jaise functions, variables, classes waghera.
# Ye code hum baad mein kisi aur program mein import karke reuse kar sakte hain.

# 🔧 Soch le module ek dabba hai jisme tools (functions, variables) rakhe hain. Tu jab chaahe, wo dabba uthake kahin bhi use kar sakta hai.

# 📂 2. Do tarah ke modules hote hain:
# ✅ Built-in Modules – Python ke sath hi milte hain
# Jaise:

# math – maths ke formulas ke liye
# random – random numbers ke liye
# datetime – date aur time ka kaam
# os – system ke saath interaction
# sys – interpreter se related info

# Example:

# import math
# print(math.sqrt(16))  # Output: 4.0


# 🧑‍💻 User-defined Modules – Tu khud banata hai .py file
# Jaise:

# # file: mymodule.py
# def greet(name):
#     return f"Hello, {name}!"
# Aur jab chaahe:


# import mymodule
# print(mymodule.greet("Bhai"))  # Output: Hello, Bhai!



# 📥 3. Module ko import kaise karte hain?

# 🔸 Basic:
# import math

# 🔸 Specific function:
# from math import sqrt
# print(sqrt(25))

# 🔸 Alias name:
# import math as m
# print(m.pi)

# 🔸 Sab kuch import karna:
# from math import *
# print(sin(90))
# (Yeh waala avoid karna best hota hai)

# 💡 4. __name__ == "__main__" ka funda kya hai?
# Jab tu koi module run karta hai directly, tab uska __name__ hota hai "__main__"
# Lekin agar tu import karta hai, to __name__ hota hai module ka naam.

# # mymodule.py
# def test():
#     print("Testing...")

# if __name__ == "__main__":
#     test()
# Agar mymodule.py ko direct run karega to chalega
# Agar import karega, to test() call nahi hoga


# 📌 Short Summary:

# Feature	                Description
# Module	                Python file (.py)
# Built-in Module	        Python ke sath aate hain
# User-defined Module       Tu khud banata hai
# import	                Kisi module ko use karne ka tareeka
# __name__ == "__main__"	Direct vs import run ka check










# Third-party Modules in Python kya hote hain?
# Third-party modules wo Python libraries hoti hain jo:

# Python ke default installation ke saath nahi aati.
# Lekin aap internet se install kar ke use kar sakte ho (usually via pip).
# Ye modules kisi aur developer/community ne banaye hote hain (na ki Python core team ne).

# 📥 Kaise install karte hain?
# Python ka pip tool use hota hai third-party modules install karne ke liye.
# pip install module-name

# Example:

# pip install numpy

# 🎯 Famous Third-party Modules ke Examples:

# Module	    Use Case
# NumPy	        Maths, arrays, matrix operations
# Pandas	    Data analysis, data manipulation
# Requests	    Web APIs se data fetch karne ke liye
# Flask	        Web applications banane ke liye (web dev)
# Django	    Full web framework
# Matplotlib	Graphs and charts plot karne ke liye
# OpenCV	    Image processing and computer vision
# BeautifulSoup	Web scraping (web page se data nikalna)
# Scikit-learn	Machine learning ke liye tools

# 💡 Python ke Module Types Quick Recap:

# Type	Example	Install Required?
# Built-in	math, os	❌ Nahi
# User-defined	Khud ka likha	❌ Nahi
# Third-party	numpy, pandas	✅ Haan, pip se











# "Importing Modules in Python" – Explained like a Desi
# Python mein module matlab ek .py file jisme kuch functions, variables, ya classes likhe hote hain.
# Agar wo code baar-baar chahiye, to import karke use kar lete hain. 👇

# ✅ 1. Basic Import
# Sabse simple tareeka.

# import math
# print(math.pi)   # Output: 3.1415...
# math module pura load hota hai.

# Access karne ke liye math. lagana padta hai har baar.

# ✅ 2. Import with Alias (Nickname dena 😄)

# import numpy as np
# print(np.array([1, 2, 3]))
# numpy ka alias np rakha, likhne mein easy ho gaya.

# ✅ 3. Import Specific Things Only (Targeted Import)

# from math import sqrt, pi
# print(sqrt(16))  # 4.0
# print(pi)        # 3.14159...
# Sirf sqrt aur pi import kiya.
# Memory aur time dono bacha liya.

# With Alias:

# from math import sqrt as s, pi as p
# print(s(25))  # 5.0
# print(p)      # 3.14159...

# ⚠️ 4. Import Everything (from module import *)

# from math import *
# print(sin(0))  # 0.0
# Ye wildcard import hai.
# Sab kuch ek sath import ho gaya (pi, sin, cos, sqrt, etc.)
# Not recommended for big modules — memory waste + confusion hota hai.

# 🔍 Comparison Table

# 🔧 Style	            🧠 Bytecode Impact	👀 Readability	⚡ Performance
# import module	          ✅ Minimal	         ✅ Clear	    ✅ Fast
# from module import foo  ✅ Lean & Clear	 ✅ Clear	    ✅ Efficient
# from module import *	  ❌ Bigger	         ❌ Confusing	❌ Slower

# 🧵 Bonus: Lazy vs Eager Loading
# import math         # Lazy: only loads `math`, actual functions run later
# from math import *  # Eager: loads EVERYTHING immediately into memory
# Lazy = memory saver, clean
# Eager = memory waste, conflicts ho sakte hain









# Bhai yeh ek "namespace collision" ka classic example hai — aur full desi style mein bolun to:
# "Do modules ek hi naam ke item lekar aa gaye, aur Python confuse ho gaya ki kaun sa lena hai!" 😵‍💫

# 🔥 Scene Samajh:
# Tu likhta hai:

# from math import *
# from numpy import *
# print(pi)
# Ab math bhi pi deta hai (math.pi = 3.141592653589793)
# Aur numpy bhi pi deta hai (numpy.pi = 3.141592653589793 — but numpy ka apna object hota hai)

# 🤔 Toh print(pi) kya karega?
# 👉 Jab tu from numpy import * likhta hai baad mein, to:

# Pehle math ka pi load hota hai.
# Fir numpy ka pi uske upar overwrite ho jaata hai.
# Final result: numpy.pi print hota hai — but coincidentally wo bhi same value deta hai!

# 💥 Actual Problem: Namespace Overlap
# Jab tu wildcard import (*) karta hai, to:
# Python sab kuch current namespace mein daal deta hai.
# Agar do modules mein same naam hota hai (like pi), to last one jeet jaata hai.
# Tu confuse ho jaata hai: yeh pi kiska hai bhai?

# 🧠 Python kya karta hai?
# Step-by-step:

# from math import *
# ➤ pi aata hai from math.

# from numpy import *
# ➤ pi phir aata hai, math wala overwrite ho gaya.

# print(pi)
# ➤ numpy.pi print hota hai, but coincidentally same value deta hai.

# ✅ Best Practice:
# 🚫 Never do: from module import *
# ✅ Instead:

# import math
# import numpy as np

# print(math.pi)      # 3.141592653589793
# print(np.pi)        # 3.141592653589793 (but float64 type)
# This way tu clearly jaanta hai pi kis module se aaya.










#  Iterable Unpacking
# ✅ Unpacking a Tuple

# student = ("Ali", 20, "Lahore")
# name, age, city = student
# print(f"Name: {name}, Age: {age}, City: {city}")

# 📤 Output:
# Name: Ali, Age: 20, City: Lahore

# ✅ Unpacking with Asterisk (*)
# numbers = [10, 20, 30, 40, 50]
# first, *middle, last = numbers

# print("First:", first)
# print("Middle:", middle)
# print("Last:", last)

# 📤 Output:
# First: 10
# Middle: [20, 30, 40]
# Last: 50
# ⭐ * bacha hua data capture karta hai as a list.










# Immutable Type Example (Pass by Value feel)
# Jaise: int, float, str, tuple
# Inmein original value change nahi hoti function ke andar.

# def change_name(name):
#     name = "Ali"
#     print("Inside Function:", name)

# my_name = "Ahmed"
# change_name(my_name)
# print("Outside Function:", my_name)

# 🔎 Output:
# Inside Function: Ali
# Outside Function: Ahmed
# ✅ Kyun? str immutable hoti hai. Function mein change hone ke bawajood original my_name change nahi hua.

# ✅ Mutable Type Example (Pass by Reference feel)
# Jaise: list, dict, set
# Inmein original value change ho sakti hai function ke andar.

# def update_marks(marks):
#     marks[0] = 100

# my_marks = [50, 60, 70]
# update_marks(my_marks)
# print("Outside Function:", my_marks)

# 🔎 Output:
# Outside Function: [100, 60, 70]
# ✅ Kyun? list mutable hoti hai. Function ne original list ke first element ko update kar diya.










# Generator Functions

# ✅ Simple Generator Example

# def fruit_generator():
#     yield "🍎 Apple"
#     yield "🍌 Banana"
#     yield "🍇 Grapes"

# fruits = fruit_generator()

# print(next(fruits))  # 🍎 Apple
# print(next(fruits))  # 🍌 Banana
# print(next(fruits))  # 🍇 Grapes
# ⛔ If you call next(fruits) one more time, you'll get:


# StopIteration

# ✅ Use Case: Even Number Generator

# def even_numbers(limit):
#     num = 0
#     while num <= limit:
#         yield num
#         num += 2

# for even in even_numbers(10):
#     print(even, end=' ')
# 📤 Output:

# 0 2 4 6 8 10
# ⚡ Memory efficient loop — no big list created!







# "Jo ordered aur sequence type cheezein hoti hain ➔ usme indexing hoti hai!"
# Data Type	   Indexing?	Example Access
# String	     ✅	      "hello"[1] ➔ 'e'
# List	         ✅	      [10,20,30][2] ➔ 30
# Tuple	         ✅	      (1,2,3)[0] ➔ 1
# Range	         ✅	      list(range(5))[3] ➔ 3
# Set	         ❌	       No indexing
# Dict	         ❌	      Access by key, not index
# Generator	     ❌	       No indexing
