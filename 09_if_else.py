# if else
x=int(input("Enter your age:"))
if x>19:
    print("you can drive car")
    print("Yeh I can drive the car")
else:
    print("You can't drive the car")
    print("ohno! I don't drive the car")
    # if else elif
shoes_price=500
my_buget=300
print(int(input("Enter your buget first:")))
if shoes_price-my_buget >= 700:
    print("you can buy shoes")
    print("Hey! I can buy the shoes")
elif shoes_price-my_buget<=700:
    print("Now I can buy shoes")
else:
    print("You can't buy the shoes")
    print("Ohno my buget is less I can't buy the shoes")

# create one more now
num=int(input("Enter your number first:"))
if num<0:
    print("The number is negative")
elif num==999:
    print("Number is greater")
elif num==0:
    print("Number is zero")
else:
    print("Number is positive")


