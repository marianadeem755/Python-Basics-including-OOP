num=int(input("Enter the number first:"))
if num < 0:
    print("The number is negative")
elif num<20:
    if num>10 and num<19:
        print("Number is  equal to 18")
    elif num>18:
        print("Num is greater than 18")
    else:
        print("Number is zero")

else:
    print("Number is greater than or equal to 20")

# now create another nested loops
num=int(input("Enter your number first"))

if num<10:
    print("The num is very small")
elif num>40:
    if num>=45 and num==50:
        print("num is equal to 50")
    elif num!=45:
        print("num is not equal to 45")
    else:
        print("num is equal to 1")
else:
    print("num is less than 20")

num=50
if num<10:
    print("The num is very small")
elif num>40:
    if num>=45 and num==50:
        print("num is equal to 50")
    elif num!=45:
        print("num is not equal to 45")
    else:
        print("num is equal to 1")
else:
    print("num is less than 20")