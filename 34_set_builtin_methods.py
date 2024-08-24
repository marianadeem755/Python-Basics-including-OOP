# isdisjoint
s1={"maleshia","japan","france","germany","spain"}
s3={"india","switzerland","pakistan","japan","france","germany","spain"}
s2={"japan","france","germany","spain","india","switzerland","pakistan"}
s3=s1.isdisjoint(s2) # Is di joint tells whther their is any common value present or not if present then it gives false means it is not is dis joint
# # while if their is no common value present then it gives True isdisjoint means they are diffrent from each other
print(s3)

# Is superset
s4=s1.issuperset(s2)
print(s4)
s5=s2.issubset(s1)
print(s5)
s6=s3.issubset(s1)
print(s6)
s7=s1.issuperset(s3)
print(s7)
# the subset is when all the values of superset in other set and donot contains the non common values similar is case with superset

# add() # It does not create the new set because it adds the item in the existing set
s1.add("pakistan")
print(s1)
s1.update(s2)
print(s1)

# Remove or discard
s1.discard("france")
print(s1)
# Removes and discard is used to remove  the element from the set of which we donot want
# The Differnce between remove and discard is that when the item is not present in the set then remove throughs the error while the discard does not throws the error

# Pop
s8=s1.pop()
print(s8)
# It pops any of the element and it creates the new set bcz it pops any of the item from the original set
del(s1)
s1.clear()
print(s1)
# The diffrence between del and clear is that del removes whole set along with items while clear removes the items not the set
if "france" in s1:
    print("yes")
else:
    ("No")