tup=(23,34,56,67,89,93,103)
# print(tup)
# print(type(tup), tup)

tupl=(85, )
print(type(tupl))

print(tup[2:3])
print(tup[::2]) # is mn woh value bhi included hai jis ki proper pairing nhi ho rhi # yhan pai hum nai kuonkai last value ki limit nhi btai indexing sai is liay python end tak lai ga is ko
print(tup[::3])
print(tup[::4])
print(tup[::5])
print(tup[::6])

# Negative indexing
print(tup[-4:-3])
print(tup[-5:-3])

# Three indexes negative slicing
print(tup[-6:-1:2]) # likhna hum left side sai hi shroo kertai hn
print(tup[-5:-2:3]) #In negative Indexing when we take start from left to right and left one value from the left
print(tup[-4:-2:2]) #Remember we have to left one value before counting from the end as we do in positive indexing

if 89 in tup:
    print("89") # hum is ko print kernai kai liay string mn bhi likh saktai hn and without string bhi likh saktai hn
else:
    print("NO 89")