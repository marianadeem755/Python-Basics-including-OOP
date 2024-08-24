index=0
marks=[12,34,56,78,96,69,90]
for mark in marks:
    print(mark)
    if index==4:
        print("awesome, Maria")
    index+=1

# now we can do the above of code using enumerate function
marks=[12,34,56,78,96,69,90]
for index , mark in enumerate(marks):
    print(mark)
    if index==4:
        print("awesome, Maria")

names=["Maria","shazia","jaweria","tayyaba","sadia","tuba","maryam"]
for index,name in enumerate(names):
    print(index,name)
    if name=="shazia":
        print("Extemely amazing")


names=["Maria","shazia","jaweria","tayyaba","sadia","tuba","maryam"]
for name in (names):
    print(name)
    if name=="shazia":
        print("Extemely amazing")
