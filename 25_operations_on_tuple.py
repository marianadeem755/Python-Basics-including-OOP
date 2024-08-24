# 1st Method
tupl=("January","Febrauary","March","April","May","June","July","August","May","SEptember","Octuber","November","May")
tup=list(tupl)
tup.append("December")
print(tup)

# 2nd Method
tup.pop(2)
tup[2]="Favourite"
# print(tup)

tupl=tuple(tup)
print(tupl)
print(tupl.count("May"))
tup=(12,22,33,35,45,12,67,89,35,90,76,54,12,35,98,76,35,12,51,35,12)
res=tup.index(12, 5, 15) # First value represents that number of which occurance we have to take
print(res)
ind=tup.index(35,6,20)
print(ind)
print(tup.count(35))
print(len(tup))