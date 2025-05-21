# Exception Handling Kya Hai?
# Exception handling ka matlab hai: unexpected errors ko detect karna aur unhe handle karna taake program ruk na jaye.
# Agar koi error (jaise ZeroDivisionError, TypeError, ValueError, etc.) 
# aaye, to program normally crash kar jata hai. Lekin try-except block use karke hum us error ko pakad kar, 
# uske liye kuch alternative karwa sakte hain.


# Kab Aur Kyun Use Karte Hain?
# Kab: Jab koi aisi line ho jisme error aane ka chance ho (e.g. user input, file handling, division, API call, database connection)
# Kyun: Taake program crash na ho aur user ko meaningful message diya ja sake ya fallback code chal sake.


# Syntax of Exception Handling

# try:
    # risky code
# except ExceptionType:
    # error hone par ye chalega
# else:
    # agar koi error na ho to ye chalega
# finally:
    # chahe error aaye ya nahi, ye hamesha chalega


# Example: ZeroDivisionError

# try:
#     a = int(input("Enter a number: "))
#     result = 10 / a
#     print("Result is:", result)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Please enter a valid number!")
# else:
#     print("Division successful.")
# finally:
#     print("Execution completed.")


# 💡 Common Built-in Exceptions

# Exception Name	   Cause
# ZeroDivisionError	   Divide by 0
# ValueError	       Invalid type for a function
# TypeError	           Operation on incompatible types
# IndexError	       List index out of range
# KeyError	           Dictionary key not found
# FileNotFoundError	   File does not exist
# ImportError	       Module not found


# 🧠 Custom Exceptions
# Agar aapko apne rules ke mutabiq custom error banana ho, to:

# class MyError(Exception):
#     pass

# try:
#     raise MyError("Something went wrong!")
# except MyError as e:
#     print(e)


# 🎯 Best Practices
# Sirf specific exceptions pakdo (except ValueError ✅, except: ❌)
# finally block ka use karo cleanup ke liye
# else ka use karo jab try block successful ho
# logging ka use karo print ke bajaye production mein








# What is NoReturn in Python?
# NoReturn is a type hint from the typing module used to indicate that a function never returns
#  (i.e., it either raises an exception or exits the program).

# from typing import NoReturn

# def fatal_error(msg: str) -> NoReturn:
#     raise SystemExit(msg)

# 🔸 When to Use NoReturn

# Use it when:
# A function always raises an exception
# A function calls exit() or sys.exit()
# You want to make the control flow clearer to type checkers like mypy, Pyright


# 🔹 🧠 Why Not Just Use None?
# None means the function returns, but returns None.

# def greet() -> None:
#     print("Hello")
#     # This function returns None implicitly
# ⚠️ But this returns — it doesn’t match functions that never return.

# 🔸 ✅ Alternatives to NoReturn

# Alternative	Use When
# -> None	Function returns nothing but still completes execution
# -> Never	New in Python 3.11+, better replacement for NoReturn
# @overload + NoReturn	For overloads that signal a function never returns for some inputs
# exit() / raise	Actual statements used to exit, not a replacement — NoReturn is for typing only


# 🔹 ✅ Never vs NoReturn (Python 3.11+)

# from typing import Never  # Python 3.11+

# def crash() -> Never:
#     raise RuntimeError("boom!")
# ✅ Never is the modern name and will replace NoReturn eventually.

# 🔸 Example of All

# from typing import NoReturn

# def always_fails() -> NoReturn:
#     raise Exception("Oops!")

# def nothing_returns() -> None:
#     print("I return None")

# from typing import Never  # Python 3.11+

# def newer_way() -> Never:
#     raise SystemExit()


# 🔍 Summary
# Concept	Means	                        Returns?	         Python Version
# None	    Function returns nothing	    ✅	                  Any
# NoReturn	Function never returns	        ❌	                 Python 3.6+
# Never  	Same as NoReturn, modern style	❌	                 Python 3.11+

# Agar tum Python 3.11 ya upar use kar rahe ho, to Never is the better alternative to NoReturn.