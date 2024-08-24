
# Python Decorators
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:
# Basic syntx od Decorators
# @decorator_function
# def my_function():
#   pass
# The @decorator_function notation is just a shorthand for the following code:
# def my_function():
#    pass
# my_function = decorator_function(my_function)
# One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:
# Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

# In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior 
#without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.

def greet(fx):
    print("First Method")
    def mfx(*args, **kwargs):
       print("Good Morning, What do you want to do")
       fx(*args, **kwargs)
       print("Thnaks for taking time to run this function")
    return mfx
@greet
def hello():
       print("Hello World!")
hello()
@greet
def add(a, b):
     print(a+b)
add(45,78)
print("================================================")

def greet(fx):
    print("Second Method")
    def mfx(*args, **kwargs):
       print("Good Morning, What do you want to do")
       fx(*args, **kwargs)
       print("Thnaks for taking time to run this function")
    return mfx
@greet
def hello():
       print("Hello World!")
hello()
@greet
def add(a, b):
     print(a+b)
add(45,78)

def greet(fx):
    def mfx(*args, **kwargs):
        fx(*args, **kwargs)
    return mfx
@greet
def hello():
    print("Hello world")
@greet
def add(x,y):
    print(x+y)


print("Good Morning, What do you want to do")
hello()
add(32,45)
print("Thnaks for taking time to run this function")

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning, what do you want to do now")
        fx(*args, **kwargs)
        print("Thanks for taking time to run this function")
    return mfx
@greet
def hello():
    print("Hello world!")
hello()
@greet
def add(a, b):
    print(a+b)
add(23,45)

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def logging_group(fx):
    def mkfx(*args, **kwargs):
       logging.info(f"Currntly the {fx.__name__}, args={args} and kwargs={kwargs}")
       result=fx(*args, **kwargs)
       logging.info(f"{fx.__name__} and return the result {result}")
       return result
    return mkfx
@logging_group
def addition_func(x,y):
    return x+y
addition_func(19,78)


import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def logging_func(fx):
    def mkfx(*args, **kwargs):
        logging.info(f"The function calling {fx.__name__} with args={args} and kwargs={kwargs}")
        result=fx(*args, **kwargs)
        logging.info(f"The function calling {fx.__name__} with result returns {result}")
        return result
    return mkfx
@logging_func
def sub_func(a,b):
    return a-b
sub_func(32,12)