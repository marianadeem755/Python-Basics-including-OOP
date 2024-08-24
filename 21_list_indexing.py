names=["maria","shazia","javeria","tayabba","maham","areej","bisma","kinza","maliha","sughra"]
# print(names[1:-2])
# # print(names[1:len(8-2)])
# print(names[1:6])

# jumping index
print(names[0:10:6])
#list comprehension
lst=[i for i in range(20)]
print(lst)
lst1=[i*i for i in range(20)]
print(lst1)
lst2=[i*i for i in range(20) if i%2==0]
print(lst2)
lst3=[i for i in range(20) if i%2==0]
print(lst3)