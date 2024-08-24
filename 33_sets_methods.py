set1={90,87,76,54,43,32,12,67} 
set2={13,78,65,34,21,32,54,90}
# union
uni=set1.union(set2)
print(uni)
# intersection
int=set1.intersection(set2)
print(int)
# update
# the intersection update firstly take the intersection of both the sets and then update theset1 based on set2 means the elements common in both sets
set1.intersection_update(set2)
print(set1)
# the update method just updates the second set
set1.update(set2) #it updates the first set by adding all the elements of the second set to the first one
print(set1)
s={"tokyo","pakistan","india","bangladesh","japan"}
s1={"switzerland","germany","italy","france","tokyo"}
s.update(s1)
print(s)
s.intersection_update(s1)
print(s)

# symmetric_diffrence and symmetric_difference_update
# in symmetric difference we can take only those values which is not common among two sets
# symmetric difference updata firstly takes the symmetric difference and then it updates the set
s3=s.symmetric_difference(s1)
print(s3)
s.symmetric_difference_update(s1)
print(s)


# symmetric diffrence takes those values which are not common among two sets means it does not takes the inetersection 
# the symmetric diffrence returns a new set bcz it updates the original one and another one 
# symmetric diffrence update does not returns the new set bcz it modifies or updates the original one
s2={"behreen","italy","france","germany","spain"}
s3={"India","swizerland","bangladesh","pakistan","italy"}
# s4=s2.symmetric_difference(s3)
# print(s4)
# s2.symmetric_difference_update(s3)
# print(s2)

# Diffrence and diffrence update
s4=s2.difference(s3) # It took the diffrence of First set with other set and excludes the common value
print(s4)
s2.difference_update(s3)
print(s2) # the update donot creates the new set becuse it updates the original set