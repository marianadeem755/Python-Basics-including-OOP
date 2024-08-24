tup=(12, 16, 90)
print(tup)
print(type(tup), tup)

# when we write single value in the tuple than it is necessary to add coma after the value other than the python becomes confused and not understand the type tuple and gives int or float
tuple=(15, )
print(tuple)
print(type(tup))

tuple=(15)
print(tuple)
print(type(tup))

tupler=(34,78,98,67,52,12) #Jitnai ka diffrence lena hai woh jhan sai count kerna start kerain gai us mn hi included ho ga then next...
print(tupler[2:6])
print(tupler[3:4])
print(tupler[4:5])
print(tupler[::2])
print(tupler[::3])
print(tupler[::4])

# Negative Indexing
print(tupler[:-4])
print(tupler[-4:-3])
print(tupler[-2:-1]) #Jo lani ho gi values us to slicing mn next portion mn likhna hai
print(tupler[-3:])

tupe=("catto",78,90,67,12)
print(tup)
print(type(tup), tup)

tupl=(12,16,19,23,45,67,89,90,93,522,55)
print(tupl[::3])
print(tupl[::5])
#print alternative values
print(tupl[1:9:3]) #agar agli wali values mukamal na houn toh woh nhi lii jain gi
print(tupl[-7:-1:2]) #negative index mn ulta hisab hota hai jo phli index ki value hoti hai us ki value us sai aak phlai tak letai hn jesai positive index mn hota haia
print(tupl[-9:-2:3]) # negative indexing mn ulta hisab hota hai is mn agar akhari wali value pair pora na bhi ho to phir bhi lai li jati hai
print(tupl[-8:-1:2]) #using negative indexes
# use i keyword
# Check for item
if 67 in tupl:
    print("yes")
else:
    print("No")