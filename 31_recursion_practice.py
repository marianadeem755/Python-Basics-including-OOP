def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))


def fibonacci(fn):
    if fn==0:
        return 0
    elif fn==1:
        return 1
    else:
        return (fibonacci(fn-1)+fibonacci(fn-2))
n=int(input("Enter the number first of which fibonacci you want to take:"))
print(fibonacci(n))