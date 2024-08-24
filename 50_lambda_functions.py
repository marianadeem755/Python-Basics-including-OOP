def multipl(x):
    return x*4
print(multipl(52))

# lets convert this into lambda function
multipl=lambda x:x*4
print(multipl(52))

# create the double function
doubl=lambda x:x*x*2
print(doubl(3))

cube=lambda x:x*x*x*2
print(cube(65))

multi_val=lambda x:x*x*x*5/3
print(multi_val(67))

avg=lambda x:x*x*x*7/9
print(avg(67))

def appl(fx, value):
    return 9+fx(value)
print(appl(lambda x: x*x, 3))

def avg(fx, number):
    return 45 + fx(number)
print(avg(lambda x:x*x/x, 2))

def diff(fx, val):
    return 67 - fx(val)
print(diff(lambda x:x*x*x-5, 4))

# x=input("Enter the name first:")
# y=input("Enter your roll no:")
# def interview(x,y):
#     print(f"your name is {x}")
#     print(f"your rollno is {y}")
#     for x,y in interview:
#         print(x,y)
#     if interview=="N":
#         print("stop")
#     else:
#         print("you can't tell you name and roll no in this segemnet")
# interview(x,y)
# def interview():
#     while True:
#         x=input("Enter the name first:")
#         y=input("Enter your roll no:")
#         stop=input("Do you want to quit the program Than press N otherwise leave it empty: ")
#         if stop.upper()=="N":
#             print("Stop")
#             break
#         else:
#             print(x,y)
# interview()
# def func():
#     value=int(input("Enter the value 3 or 7: "))
#     if value==3:
#         print(7)
#     else:
#         print(3)
# func()

# mapping tooks the key value pair
# mapping={3:7, 7:3}
# value=int(input("Enter the value 3 or 7: "))
# print(mapping.get(value, "Invalid value Entered"))

