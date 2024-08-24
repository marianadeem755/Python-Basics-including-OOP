num=int(input("Enter the input number first: "))
while num>100:
    num=int(input("Enter the input number first: "))
    break
print("number becomes greater")
print("we are out of loop now")



for i in range(1,100):
    print(i)
    if i==90:
        print("skip the iteration")
        continue
print("Now we've done")

for num in range(0,50):
    print("5 X", num+1, "=",5*(num+1))
    if num==9:
       break

for num in range(0,100):
    print("2 X", num, "=",2*(num))
    if num==20:
       break
print("we are done with table of 2")


#do while loop
i=0
while True:
    print(i)
    i=i+1
    if i>=90:
        break
print("thi is it!")


i=1
while True:
    print(i)
    i=i+1
    if i>=90:
        break
       