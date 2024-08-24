# required arguments 
def getvalue(a,b):
    average=(a+b)/(2)
    print("Lets print the average:", average)
getvalue(6,12)

# Default argument
def myvalue(a=15, b=45):
    average1=(a+b)/2
    print("The average of the a and b is:", average1)
myvalue(a=22)

#keyword argument
def mariavalues(c=95, d=42, e=67):
    average2=(c+d+e)/2
    print("The average of the a and b is:", average2)
myvalue(15, 32)

def mynames(name1="Maria",name2="javeria",name3="kinza",name4="Mailha"):
    print("Names in the list are:", name1,name2,name3,name4)
mynames("Shazia")

def average(*numbers):
    sum=0
    for sum in numbers:
       print("The average of the numbers are:", sum/len(numbers))
average(45,76,89,23)

def average(*numbers):
    sum=0
    for i in numbers:
       sum=sum+i
    print("The average of the numbers are:", sum/len(numbers))
average(45,76,89,23)

def name(**names):
    print("Hello!", name=["mname"], name=['nname'], name=['sname'])
name(mname="Maria", nname="Nadeem", sname="Shazia")

def myname(**names):
    print("Hello!", names['nname'], names['mname'], names['sname'])
myname(nname="Nadeem", mname="Maria", sname="Shazia")

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        return sum/len(numbers)
    #    print("The average of the numbers are:", sum/len(numbers))
c=average(45,76,89,23)
print(c)