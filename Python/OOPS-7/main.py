# PILLARS OF OOPS
# ABSTRACTION
# ENCAPSULATION
# POLYMORPHISM
# INHERITANCE




# ## ✅ What is **Abstraction** in Python OOP?
# ### 📘 **Definition:**
# > **Abstraction** means **hiding the internal implementation details** and **showing only the essential features** to the user.

# In simpler terms:
# > "User ko **sirf kaam ka part** dikhana, aur **andar ka logic chhupa lena**."

# ## 🧠 Real-Life Example (Desi Style):
# 🔌 When you **turn on a fan**, you just press a button. You don’t need to know:
# * How current flows,
# * How the motor spins,
# * How voltage is managed.
# ➡️ That’s **abstraction**: hide internal complexity, expose only what's needed.

# ## 🔹 Why Use Abstraction?
# * ✅ Improves **code readability**
# * ✅ Makes code **easier to maintain**
# * ✅ Enforces **security** and **controlled access**
# * ✅ Promotes **modular design**

# ## 🔹 How to Achieve Abstraction in Python?

# Python provides **abstraction** using:

# 1. **Abstract Classes**
# 2. **Interfaces (via abstract base classes)**
# 3. **Encapsulation (indirectly supports abstraction)**

# ## 🔷 1. **Abstract Classes in Python**
# To create abstract classes, we use:
# * `ABC` → Abstract Base Class
# * `@abstractmethod` → Marks methods that **must** be implemented by child classes

# ### ✅ Example:

# from abc import ABC, abstractmethod

# class Shape(ABC):  # Abstract class
#     @abstractmethod
#     def area(self):  # Abstract method
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# c = Circle(5)
# print(c.area())  # Output: 78.5

# ➡️ You **cannot create an object** of `Shape`. Only subclasses that implement `area()` can be instantiated.

# ## 🔷 2. **Properties of Abstraction**

# | Property                      | Description                                         |
# | ----------------------------- | --------------------------------------------------- |
# | **Hides Implementation**      | Only the interface is exposed, not the inner logic  |
# | **Enforces Method Structure** | Child classes must implement specific methods       |
# | **Prevents Instantiation**    | Abstract classes **can’t** be directly instantiated |
# | **Promotes Modularity**       | Encourages writing reusable, modular code           |
# | **Improves Security**         | Hides sensitive operations from the outside world   |

# ## 🔷 3. **Multiple Abstract Methods**

# You can define multiple abstract methods in an abstract class:

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self): pass

#     @abstractmethod
#     def stop_engine(self): pass

# Any subclass must implement **all** abstract methods.


# ## 🔷 4. **Partial Abstraction**
# An abstract class can also contain **concrete methods** (with logic):

# class Device(ABC):
#     @abstractmethod
#     def power_on(self): pass

#     def greet(self):
#         print("Welcome to the device!")

# ## 🔷 5. **Abstract Class vs Interface**

# Python doesn’t have formal interfaces like Java, but abstract base classes **act like interfaces**.

# | Feature             | Abstract Class            | Interface (ABC)               |
# | ------------------- | ------------------------- | ----------------------------- |
# | Can have methods    | ✅ Yes (abstract + normal) | ✅ Yes (only abstract usually) |
# | Can have attributes | ✅ Yes                     | ✅ Yes                         |
# | Instantiable?       | ❌ No                      | ❌ No                          |
# | Used via            | `abc.ABC`                 | `abc.ABC`                     |

# ## 🔷 6. **Abstract Properties (Advanced)**
# You can even create abstract **properties**:

# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @property
#     @abstractmethod
#     def salary(self):
#         pass

# Subclasses must implement the property `salary` using `@property`.





# ✅ What is Encapsulation in Python?
# 📘 **Definition:**
# > **Encapsulation** is the process of **bundling data (variables)** and the **methods (functions)** that 
# operate on that data into a **single unit (class)**, and **restricting direct access** to some of the object’s components.

# 💡 Desi Style Explanation:

# > "Encapsulation matlab **sab kuch ek dabbe (class)** ke andar bandh kar dena — data aur us pe kaam karne wale function bhi.
#  Aur agar zaroorat na ho, to us dabbe ko lock kar dena (yaani private/protected banana)."

# 🧠 Real-Life Analogy:
# 📦 A **medicine bottle**:
# * You can take the medicine (public method),
# * But you can’t **open the formula or mix ingredients** (private/protected data).
# * The company keeps that secret = **data protection (encapsulation)**.

# 🔹 Key Goals of Encapsulation

# | Goal                 | Benefit                                  |
# | -------------------- | ---------------------------------------- |
# | Data Hiding          | Prevent unauthorized access to variables |
# | Data Protection      | Avoid accidental changes                 |
# | Controlled Access    | Use getters and setters to manage access |
# | Code Maintainability | Reduces complexity                       |

# 🔧 How is Encapsulation Implemented in Python?
# 🔹 1. **Using Classes**
# Encapsulation begins when you create a class that combines **data + behavior**.

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def show_balance(self):
#         return self.balance

# Here, `balance` and `show_balance()` are **encapsulated** inside the class.

# 🔹 2. **Access Modifiers in Python**
# Python doesn’t have strict **private/protected** keywords like Java or C++, but uses **naming conventions**:

# | Type          | Syntax   | Meaning                                                |
# | ------------- | -------- | ------------------------------------------------------ |
# | **Public**    | `name`   | Accessible from anywhere                               |
# | **Protected** | `_name`  | Suggests internal use (can be accessed, but shouldn’t) |
# | **Private**   | `__name` | Name mangling makes it harder to access directly       |

# 🧪 Example with All Types:

# class Person:
#     def __init__(self):
#         self.name = "Ravi"        # public
#         self._age = 30            # protected
#         self.__salary = 50000     # private

#     def show(self):
#         print(self.name, self._age, self.__salary)

# p = Person()
# print(p.name)        # ✅ Public - Accessible
# print(p._age)        # ⚠️ Protected - Can access, but not recommended
# # print(p.__salary)  ❌ Private - Will raise error
# print(p._Person__salary)  # ✅ Name mangling to access private

# 🔒 Getters & Setters (Controlled Access)

# Encapsulation recommends accessing private data via methods:

# class Employee:
#     def __init__(self):
#         self.__salary = 50000

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, amount):
#         if amount > 0:
#             self.__salary = amount

# 🔐 This protects the internal variable from being set to invalid values.

# 🔷 Properties of Encapsulation in Python

# | Property           | Description                                           |
# | ------------------ | ----------------------------------------------------- |
# | **Data Hiding**    | Prevent direct access to internal data                |
# | **Bundling**       | Combines data and methods in one unit (class)         |
# | **Access Control** | Uses `_`, `__` to control how data is accessed        |
# | **Flexibility**    | Allows changing internal code without affecting users |
# | **Security**       | Sensitive data is hidden and protected                |
# | **Reusability**    | Clean and self-contained code makes reuse easier      |

# 🔁 Difference Between Abstraction and Encapsulation

# | Feature     | Abstraction                     | Encapsulation                     |
# | ----------- | ------------------------------- | --------------------------------- |
# | Focus       | Hiding *implementation details* | Hiding *data*                     |
# | Achieved By | Abstract classes and interfaces | Access modifiers, classes         |
# | Goal        | Show only essentials            | Protect data and bind it together |
# | Example     | Car driving logic               | Locking the fuel tank and engine  |







#  ✅ What is **Polymorphism** in Python?
#  📘 **Definition:**
# > **Polymorphism** means "**many forms**". In Python OOP, it refers to the ability of 
# **different objects** to **respond to the same method name** in **their own way**.

#  🧠 Desi Style Explanation:
# > "Polymorphism matlab ek hi naam ke kaam ko alag-alag log alag tareeke se karte hain."
# > Jaise:

# * **Teacher bolta hai "draw"** → student chalk se diagram banata hai
# * **Artist bolta hai "draw"** → canvas pe painting banata hai
# * **Software bolta hai "draw"** → screen pe graphic banta hai

# ➡️ Sab method ka naam **same** hai – `draw()`
# ➡️ Lekin kaam ka **tareeka alag-alag** hai.

# 🔹 Real-Life Example

# class Dog:
#     def speak(self):
#         return "Barks"

# class Cat:
#     def speak(self):
#         return "Meows"

# def animal_sound(animal):
#     print(animal.speak())

# dog = Dog()
# cat = Cat()

# animal_sound(dog)  # Output: Barks
# animal_sound(cat)  # Output: Meows

# 📌 Function `animal_sound()` **doesn't care** whether it's a dog or cat — it just **calls `speak()`**, and the **correct version runs**.

# 🔷 Types of Polymorphism in Python
# | Type                        | Description                                                                       |
# | --------------------------- | --------------------------------------------------------------------------------- |
# | **1. Duck Typing**          | Python philosophy: "If it looks like a duck and quacks like a duck, it’s a duck." |
# | **2. Operator Overloading** | One operator behaves differently depending on the operands                        |
# | **3. Method Overriding**    | Subclass changes behavior of parent class method                                  |
# | **4. Function Overloading** | Simulating different functions with default/variable arguments                    |


# 🔹 1. **Duck Typing**

# class PyCharm:
#     def execute(self):
#         print("Compiling and running in PyCharm")

# class VSCode:
#     def execute(self):
#         print("Running in VS Code")

# def code(editor):
#     editor.execute()

# code(PyCharm())   # Compiling and running in PyCharm
# code(VSCode())    # Running in VS Code

# ➡️ `code()` doesn't care about the class, it just calls `execute()`. That’s duck typing.

# 🔹 2. **Operator Overloading**

# Same operator, different behavior depending on data type:

# print(2 + 3)          # Output: 5 (int addition)
# print("Hello " + "AI")# Output: Hello AI (string concat)

# Python lets you define custom behavior for operators in your own classes:

# class Point:
#     def __init__(self, x):
#         self.x = x

#     def __add__(self, other):
#         return Point(self.x + other.x)

# p1 = Point(10)
# p2 = Point(20)
# p3 = p1 + p2
# print(p3.x)  # Output: 30

# 🔹 3. **Method Overriding (Runtime Polymorphism)**

# class Parent:
#     def greet(self):
#         print("Hello from parent")

# class Child(Parent):
#     def greet(self):
#         print("Hello from child")

# obj = Child()
# obj.greet()  # Output: Hello from child

# The child class **overrides** the parent’s method with its own version.

# 🔹 4. **Function Overloading (Simulated)**

# Python doesn’t support true function overloading, but we can simulate it:

# def greet(name=None):
#     if name:
#         print("Hello", name)
#     else:
#         print("Hello user")

# greet("Ravi")
# greet()

# 🔶 Properties of Polymorphism in Python

# | Property             | Description                                       |
# | -------------------- | ------------------------------------------------- |
# | **Code Flexibility** | Same interface, different behavior                |
# | **Extensibility**    | Easy to add new classes without changing old code |
# | **Dynamic Typing**   | Python doesn’t check types until runtime          |
# | **Late Binding**     | Method is resolved at runtime (not compile time)  |
# | **Simplifies Logic** | Reduces `if-else` checks based on object type     |

# 🔁 Difference Between Overloading and Overriding

# | Feature       | Overloading                                                 | Overriding                                     |
# | ------------- | ----------------------------------------------------------- | ---------------------------------------------- |
# | What it does  | Same method/operator behaves differently based on arguments | Subclass modifies the method of its superclass |
# | Happens when? | Compile-time (simulated in Python)                          | Runtime (Python supports fully)                |
# | Example       | `__add__()` for `+` operator                                | `greet()` method in subclass                   |

# * Python doesn’t support true function overloading but allows default/variable args









# ✅ What is **Inheritance** in Python?
# 📘 Definition:
# > **Inheritance** is an OOP concept where a **child class** (subclass) **inherits** methods and properties 
# from a **parent class** (superclass), allowing **code reuse** and **hierarchical relationships** between classes.

# 🧠 Desi Style Explanation:

# > "**Bete ko baap ki property milti hai** — usi tarah, child class ko parent class ka code milta hai. Baccha class apne baap (parent class)
#  ke methods aur variables use kar sakta hai, aur chaahe to unme badlav (override) bhi kar sakta hai."

# 👨‍👩‍👧 Real-Life Analogy:
# * **Parent Class** = `Vehicle`

#   * Properties: wheels, engine
#   * Methods: start, stop
# * **Child Class** = `Car`

#   * Inherits: start, stop
#   * Adds: music system, AC
# You don’t rewrite `start()` or `stop()` again in `Car`. You **reuse**.

# 🔧 Basic Syntax

# class Parent:
#     def show(self):
#         print("I am parent")

# class Child(Parent):
#     pass

# c = Child()
# c.show()  # Output: I am parent

# 🔍 Types of Inheritance in Python

# | Type             | Description                              | Diagram Style       |
# | ---------------- | ---------------------------------------- | ------------------- |
# | **Single**       | One child inherits from one parent       | A → B               |
# | **Multiple**     | One child inherits from multiple parents | A, B → C            |
# | **Multilevel**   | One child, one parent, one grandparent   | A → B → C           |
# | **Hierarchical** | One parent, many children                | A → B, A → C        |
# | **Hybrid**       | Combination of two or more types         | A → B, B → C, A → D |

# 1. 🧬 Single Inheritance

# class Animal:
#     def eat(self):
#         print("I can eat")

# class Dog(Animal):
#     def bark(self):
#         print("I can bark")

# d = Dog()
# d.eat()
# d.bark()

# 2. 🧬 Multilevel Inheritance

# class Animal:
#     def eat(self):
#         print("Eat food")

# class Dog(Animal):
#     def bark(self):
#         print("Bark")

# class Puppy(Dog):
#     def weep(self):
#         print("Weep softly")

# p = Puppy()
# p.eat()
# p.bark()
# p.weep()

# 3. 🧬 Multiple Inheritance

# class Father:
#     def skills(self):
#         print("Gardening, Programming")

# class Mother:
#     def skills(self):
#         print("Cooking, Painting")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skills()  # Output: Gardening, Programming (first parent gets priority)

# ✅ This follows **MRO (Method Resolution Order)**.

# 4. 🧬 Hierarchical Inheritance

#     def house(self):
#         print("Has a big house")

# class Son(Parent):
#     def bike(self):
#         print("Has a bike")

# class Daughter(Parent):
#     def car(self):
#         print("Has a car")

# ### 5. 🧬 Hybrid Inheritance
# Combination of any two or more types (Python supports it):

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):  # Hybrid Inheritance
#     pass

# d = D()
# d.show()  # Output: B (MRO)


# 🔁 Method Overriding in Inheritance
# Child class **modifies** inherited method:

# class Parent:
#     def show(self):
#         print("Parent class")

# class Child(Parent):
#     def show(self):
#         print("Child class")

# c = Child()
# c.show()  # Output: Child class

# 🧠 Use of `super()` Function
# Used to **call the parent class method** from child class:

# class Parent:
#     def show(self):
#         print("Parent method")

# class Child(Parent):
#     def show(self):
#         super().show()  # Call parent method
#         print("Child method")

# c = Child()
# c.show()

# 🔍 Method Resolution Order (MRO)
# * In **multiple inheritance**, Python follows **C3 Linearization** (left to right).
# * You can check it using:

# print(Child.__mro__)

# 🔐 Properties of Inheritance

# | Property                 | Description                                                |
# | ------------------------ | ---------------------------------------------------------- |
# | **Code Reusability**     | Inherited methods reduce code duplication                  |
# | **Extensibility**        | You can build on top of existing classes                   |
# | **Maintainability**      | Easier to make changes in parent and apply across children |
# | **Polymorphism Support** | Parent reference can point to child object                 |
# | **Overriding Support**   | Child can override parent methods                          |

# ⚖️ Inheritance vs Composition (Bonus)

# | Feature     | Inheritance                               | Composition                                 |
# | ----------- | ----------------------------------------- | ------------------------------------------- |
# | Structure   | "Is-a" relationship (Dog **is-a** Animal) | "Has-a" relationship (Car **has-a** Engine) |
# | Flexibility | Less flexible                             | More flexible                               |
# | Coupling    | Tightly coupled                           | Loosely coupled                             |