# global variable (is the variable which is outside the function i-e in the globe)
# local variable (is the variable which is in the function aand not globally present)
# The diffrence between global and local variable is also that the local variable destroys as the function returns while the global variable donot destroys it remains still
x=4
print(x)
def Hello():
    x=5
    print(x)
    print("Hey from Maria")
print(x)
Hello()
print(x)

x=15
print(x)
def mera_function():
    global x
    x=9
    print(x)
    # y=19
    print("This is my hand written function")
mera_function()
print(x)
# print(y)

z=67
print(z)
def good_function():
    global z
    z=98
    print(z)
good_function()
print(z)