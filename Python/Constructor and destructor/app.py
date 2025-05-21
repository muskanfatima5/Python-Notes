# 1. Constructor (Banane wala – __init__)
# 🔶 Soch lo ek class ek blueprint hai aur constructor uska naya maal tayaar karne ka kaam karta hai.
# Jab bhi tu class se ek object banata hai, to __init__() method automatic chalu ho jaata hai. Jaise hi tu bike ki chaabi ghoomata hai, engine start ho jaata hai – waise hi constructor ka kaam hai object start karna.

# ✅ Syntax aur Example:

# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

# # object banao
# s1 = Student("Rahul", 101)
# print(s1.name)  # Output: Rahul
# 🧠 Yahaan __init__() naam ka function constructor hai. self matlab khud ka reference (jo object ban raha hai).


# 🧃 Simple Words Mein:
# Feature	                Samjhauta
# Kya karta hai?	        Object ke liye setup ready karta hai
# Kab chalta hai?	        Jab object banaya jaata hai
# Kya return karta hai?	    Kuch nahi (na None, na value)
# Kya overload hota hai?	Nahi Python mein direct overload nahi kar sakte

# 🔄 Constructor Overloading?
# Python mein ek se zyada __init__() nahi ho sakte. Par hum default values ya *args, **kwargs se uska jugaad kar sakte hain.

# class Demo:
#     def __init__(self, a=0, b=0):
#         print("Sum is:", a + b)

# d = Demo(2, 3)  # 5
# d2 = Demo()     # 0


# 💣 2. Destructor (Todnewala – __del__)
# 🔶 Jaise construction ke baad kabhi na kabhi to tootna bhi hai — waise hi jab object ka kaam khatam ho jaata hai, Python usko automatically destroy kar deta hai.
# Tabhi __del__() chalu hota hai. Ye hai destructor.

# ✅ Syntax aur Example:

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} created")

#     def __del__(self):
#         print(f"{self.name} destroyed")

# s1 = Student("Aman")
# del s1  # manually destroy
# 🧠 __del__() tab chalta hai jab Python ka garbage collector object ko utha ke thikane lagata hai. Tu manually del bhi kar sakta hai.


# 🔄 Constructor vs Destructor – Desi Comparison:
# Point	Constructor (__init__)	Destructor (__del__)
# Kab chalta hai?	Jab object banta hai	Jab object mitaya jaata hai
# Kya karta hai?	Setup karta hai (initialize)	Safai karta hai (cleanup)
# Call kaise hota hai?	Automatically during creation	Automatically during deletion
# Overload kar sakte?	Nahi direct (workaround hai)	Nahi
# Use kab zaroori hota?	Jab kuch value set karni ho	Jab file close ya memory free karni ho

# 📦 Real-Life Example – Ghar Banwana aur Girana
# Scene	Constructor	Destructor
# Mistri bulaya	__init__() – ghar banana start	-
# Paint, wiring	self.kaam_karna()	-
# Ghar complete	Object ready	-
# Ghar purana ho gaya	-	__del__() – tod diya, safaai

# 📌 Bonus: Jab Destructor Automatically Nahi Chalta
# Python mein __del__() kab chalta hai ye fix nahi — garbage collector decide karta hai. Kabhi kabhi object delete hone ke baad bhi memory mein rehta hai (agar circular reference ho to).

# So, zyada heavy kaam (jaise file close, DB connection close) ke liye with ya manual clean-up zyada best hai.

# 🔚 Summary Chart – One Glance Recap
# Feature	Constructor	Destructor
# Method name	__init__(self)	__del__(self)
# Purpose	Setup karna	Safai karna
# Called when	Object banega	Object delete ya expire hoga
# Return value	Nahi	Nahi
# Custom logic	Allowed	Allowed (but lightweight)


# 🔹 1. Agar Constructor (__init__) Use Nahin Kiya:
# 🔸 Kya Hoga?
# Agar tu __init__() define nahi karta, toh bhi object banega — lekin usme koi initialization (jaise variables set karna, message print karna, etc.) nahi hoga.

# class Student:
#     pass

# s1 = Student()
# print(s1)  # Output: <__main__.Student object at 0x...>
# 🔸 Problem Kya Hogi?
# Agar tu object ke andar kuch values access karega jo set hi nahi hui (jaise self.name), toh error aayega.

# class Student:
#     pass

# s1 = Student()
# print(s1.name)  # ❌ AttributeError: 'Student' object has no attribute 'name'
# ✅ Solution:
# Constructor (__init__) ka kaam hota hai object banate hi usme data bhar dena — agar use nahi karega, toh manually sab set karna padega.

# s1.name = "Rahul"  # manually set
# 🔹 2. Agar Destructor (__del__) Use Nahin Kiya:
# 🔸 Kya Hoga?
# Agar tu __del__() use nahi karta, toh bhi Python object ko khud hi clean kar deta hai jab uski zarurat nahi hoti (garbage collection).

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Rahul")
# del s1  # object removed
# 🔸 Problem Kya Hogi?
# Normally koi problem nahi hoti.

# Lekin agar object ne kuch external resources use kiye ho (jaise: file open, database connection), aur tu destructor nahi banayega, toh wo cheeze properly close nahi hongi.

# class FileOpener:
#     def __init__(self):
#         self.file = open("data.txt", "w")

#     # __del__ define nahi kiya -> file kab close hogi, pata nahi

# f = FileOpener()
# del f  # File abhi bhi open ho sakti hai!

# ✅ Solution:
# Destructor banana accha hota hai agar resource cleanup zaruri ho. Ya use with statement instead.

# class FileOpener:
#     def __init__(self):
#         self.file = open("data.txt", "w")

#     def __del__(self):
#         self.file.close()
#         print("File closed")
  
# 🔚 Desi Conclusion:
# Scenario	            Constructor Nahi Hai 🔧	                   Destructor Nahi Hai 🧹
# Object banega?	    Haan, banega	                            Haan, chalega
# Object useful hoga?	Nahi, kyunki data nahi set hoga             Haan, lekin clean-up risky
# Kya dikkat aayegi?	AttributeError, manual kaam	                File/memory leak, unsafe
# Kab zaruri hai?	    Jab tu input le raha ho, object setup ho	Jab tu file/db/memory handle kar raha ho