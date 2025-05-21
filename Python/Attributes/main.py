# Step 1: Class Attributes vs Instance Attributes
# ⚙️ Class Attributes (Static)
# Definition: Ye woh attributes hote hain jo class level par define hote hain.

# Common for all objects of the class.

# Ek baar set kiya, to har object usko access kar sakta hai (jab tak override na kare).

# class Student:
#     school_name = "Desi Public School"  # class attribute

#     def __init__(self, name):
#         self.name = name  # instance attribute

# s1 = Student("Amit")
# s2 = Student("Riya")

# print(s1.school_name)  # Desi Public School
# print(s2.school_name)  # Desi Public School
# 💡 Note: school_name sabke liye same hai, isliye ye class attribute hai.

# 👤 Instance Attributes
# Ye object level pe define hote hain.

# Har object ka apna alag value hota hai.

# print(s1.name)  # Amit
# print(s2.name)  # Riya
# Har student ka naam alag hai, isliye ye instance attribute hai.

# 🔸 Step 2: Accessing Attributes (Dekho, Kaise Padhte Hain!)
# ✅ Access via Object:

# print(s1.name)        # Instance
# print(s1.school_name) # Class
# ✅ Access via Class (ONLY class attributes!):
# python
# Copy
# Edit
# print(Student.school_name)  # Desi Public School
# ❌ You can't access instance attributes using class directly: Student.name → Error!

# 🔸 Step 3: Modifying Attributes (Masala Part!)
# 🔁 Modifying Instance Attribute:

# s1.name = "Rahul"
# print(s1.name)  # Rahul
# print(s2.name)  # Riya (no change)
# Sirf s1 ka naam badla, s2 pe koi effect nahi.

# 🔁 Modifying Class Attribute via Class:

# Student.school_name = "Naya Desh School"
# print(s1.school_name)  # Naya Desh School
# print(s2.school_name)  # Naya Desh School
# Sabka school ek hi baar mein badal gaya 😄

# ⚠️ Modifying Class Attribute via Object (Careful!):

# s1.school_name = "Private School"
# print(s1.school_name)  # Private School
# print(s2.school_name)  # Naya Desh School
# print(Student.school_name)  # Naya Desh School
# Ab s1.school_name ban gaya ek instance attribute, class attribute se link toot gaya ❌

# 🔍 Step 4: Check Attributes Like a Pro

# print(s1.__dict__)  # shows only instance attributes
# # {'name': 'Rahul', 'school_name': 'Private School'}

# print(Student.__dict__)  # shows class attributes and methods


# 🧠 Visualization: Mind Map Style
# Student Class
# │
# ├── Class Attribute
# │   └── school_name = "XYZ"
# │
# ├── Instance (s1)
# │   └── name = "Rahul"
# │
# └── Instance (s2)
#     └── name = "Riya"


# 💡 Summary in Desi Style
# Feature	              Class Attribute	                Instance Attribute
# Defined in	          Class body	                    Inside __init__()
# Shared by	              All objects	                    Only that specific object
# Accessed via	          Class & Object	                Only via object
# Modified via Class	  Affects all objects	            N/A
# Modified via Object	  Creates a new instance attribute	Changes only that object’s value

