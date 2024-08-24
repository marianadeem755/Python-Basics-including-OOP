for i in range(10):
    print(i)
    if i==6:
        break
else:
        print("Sorry the values are not present!")

'''
jab hum if ki condition bhi break kai sath lgain gain to ya if ko run kerai ga phlai or loop break ho jai ga
or agar if ko hata dya jai r break ko sirf rehnai dya jai to ya sirf i ki value dai ga
r jab hum break statement ko bhi remove kar dain to ya
while loop ko run kerai ga jesai kai is loop and i mn har iteration pai i+1 kya hwa hai to ya 7 tak chlai ga loop
werna agar dono conditions false hon to else ko run kar dai ga
'''
i=0 
while i<8:
    print(i)
    i=i+1
    if i==6:
        print(i)
    break
else:
    ("Sorry no i exists")
print(__doc__)

for i in range(20):
    print(f"the value for the iteration no {i} is:")
    print(i)
else:
    print("Now the else is in the  loop")
    print("Now we are out of the loop")
