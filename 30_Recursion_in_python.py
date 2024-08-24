def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
print(factorial(5))
print(factorial(6))

# # Lets now create a function or program for fabonnocai sequence
def fibonacci(fn):
    if(fn==0):
        return 0
    elif(fn==1):
        return 1
    else:
        return fibonacci(fn-1)+fibonacci(fn-2)
# Get the input value from the user
n = int(input("Enter a number to get the nth Fibonacci value: "))
print(fibonacci(n))

def fibonacci(fn):
    if fn == 0:
        return 0
    elif fn == 1:
        return 1
    else:
        return fibonacci(fn - 1) + fibonacci(fn - 2)

# Get the input value from the user
n = int(input("Enter a number to get the nth Fibonacci value: "))
print(f"The {n}th Fibonacci number is {fibonacci(n)}")

