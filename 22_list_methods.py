# Append Method
l=[89,14,20,89,76,95,89]
l.append(50)
print(l)

# Sort Method
l.sort(reverse=True) # Reverse is used to sort the values of the list in the decreasing order
print(l)

# print the index of 3rd value of the list 
m=l.index(89)
print(m)

# Extend Method
l.extend([14, 98])
print(l)

e=l.count(89)
print(e)

m=l
m[0]=0
print(l)

m=l.copy()
print(m)

# Insert method is used to insert any value or replace the existing value with someother value
l.insert(1, -899)
print(l)