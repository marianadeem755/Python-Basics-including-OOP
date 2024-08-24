s={20,78,67,78,54,23,78} #sets donot main the order. They are the unordered collection of item and are enclosed as curly brackets
# print(s)

# # emp=set()
# # print(type(emp))

p={90,87,64,23,10,90,23}
# union_set=s.union(p)
# print(union_set) #addition
int_set=s.intersection(p) #multipliction and division
print("Theint set is:",int_set)
add_set=s|p #addition
print("The add set is:",add_set)
mul_set=s&p #multiplication
print("The mul set is:",mul_set)
sub_set=s.difference(p) #subtraction
print("The diff set is:",sub_set)