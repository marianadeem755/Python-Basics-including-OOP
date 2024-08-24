def cube(x):
    return x*x*x
# print(cube(2))
l=[22,34,55,67,89,92]
newl=[]
for items in l:
    newl.append(cube(items))
print(newl)

# # Lets map that function
map_func=list(map(lambda x:x*x*x, l))
map_func=list(map(cube, l))
print(map_func)

def square(x):
    return x*x
print(square(5))

l=[32,45,66,54,32,120]
new_list=[]
for items in l:
    new_list.append(square(items))
print(new_list)

new_map=list(map(square, l))
print(new_map)

new_map=list(map(lambda x:x*x, l))
print(new_map)

# filter
# In the filter function we have to use the return
def filter_func(a):
    return a>12
fil_function=list(filter(filter_func, l))
print(fil_function)

def filt_func(a):
    return a>45
new_fil=list(filter(filt_func, l))
print(new_fil)

# Reduce
from functools import reduce
def sum_func(x,y):
    return x+y
new_red=reduce(sum_func, l)
print(new_red)

from functools import reduce
def diff_func(x,y):
    return x-y
new_func=reduce(diff_func, l)
print(new_func)
