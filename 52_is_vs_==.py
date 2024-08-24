a=4
b="4"
print(a is b) # It takes the exact location in the memeory
print(a == b) # It takes the exact values

a=None
b=None
print(a is b)
print(a == b)

a="Maria"
b="Maria"
print(a is b)
print(a == b)

a=(32,41,56,78)
b=(32,41,56,78)
print(a is b)
print(a == b)

a=[32,41,56,78]
b=[32,41,56,78]
print(a is b)
print(a == b)