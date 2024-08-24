x=50
match x:
    case 0:
        print("case is zero")
    case 50:
        print("case is 50")
    case _:
        print("case does not matches")

        
        
x=30
match x:
    case 15:
        print(x, "x is 15")
    case 22:
        print("case is 22")
    case 35:
        print(x, "case is greater than 30")
    case _ :
        print(x, "case is less than 35")

x=int(input("Enter the case value first: "))
match x:
    case 0 if x<20:
        print("Case is less than 20")
    case 55 if x>50:
        print("Case is greater than 50")
    case _ if x==25:
        print("Case is equal to 25")
    case _ if x==20:
        print("case is equal to 20")
    case _ :
        print(x, "case is x")

x=int(input("Enter the case value first: "))
match x:
    case 90 if x>85:
        print(x, "Case is greater than 85")
    case 55 if x<60:
        print("Case is equal to 55")
    case 10 if x!=45:
        print("x case is not equal to 45")
    case _:
        print("x is negative")
        
