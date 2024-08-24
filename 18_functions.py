def calculateGmean(a,b):
    mean1=(a*b)/(a+b)
    print(mean1)
# def calculateGmeancd(c,d):
#     mean2=(c*d)/(c+d)
#     print(mean2)

def isgreater(a,b):
    if a>b:
       print("a is greater than b")
    else:
       print("a is less or equal to b")

def islesser (a,b):
    pass
    
a=98
b=60
if a>b:
    print("a is greater than b")
else:
    print("a is less or equal to b")
mean1=(a*b)/(a+b)
print(mean1)
calculateGmean(a,b)
isgreater(a,b)
c=56
d=87
if c>d:
    print("c is greater than d")
else:
    print("c is less or equal to d")
calculateGmean(c,d)
isgreater(c,d)
mean2=(c*d)/(c+d)
print(mean2)
