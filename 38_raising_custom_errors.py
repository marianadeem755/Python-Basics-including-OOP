x=int(input("Enter the value between 10 and 89:"))
if (x<9 or x>90):
    raise ValueError("Enter the number between 10 and 89")

x=input("Enter quit keyword otherwise you face the error:")
if x == "quit":
    print("Now you can execute the program further!")
else:
    raise ValueError("Enter quit keyword first")



