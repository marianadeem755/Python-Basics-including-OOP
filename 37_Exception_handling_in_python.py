a=input("Firstly enter the input:")
print(f"You eneter this number {a} and now i will give you the multplication table of it")
try:
    for i in range(1,11):
        num=f"{int(a)} X {int(i)}= {int(a)*int(i)}"
        print(num)
except ValueError:
    print("This is not a number . it's a string or object")
except IndexError:
    print("The list is out of the index")
print("The Multiplication table is completed now")
print("Now we stop this program right Here. Do you have any question then let me know?")

try:
    num=int(input("Firstly enter the input:"))
    a=[2,5,9]
    print(a[num])
except ValueError:
    print("No such integer is present")
except IndexError:
    print("List index is out of range")
    print("This is the program that i donot want to execute")
# Finally keyword
finally:
    print("I'm excecuted in all the cases in try, except or an error")

def func1():
    try:
       lis=[90,78,56,23]
       i=int(input("Enter the input first:"))
       print(lis[i])
       return 1
    except IndexError:
       print("List index out of the range")
       return 0
    except ValueError:
       print("This is not the value .it is a character")
       return -1
    # print("will I be able to execute")
    # finally:
    #    print("I'm executed now!")
x=func1()
print(x)
# the difference between the print statement and finally in try or except is that finally executes in all the cases while the print does not execute specially in case of function the print statement does not executed
# the print statement is executed when there is except condition(when we add print statement below except)
# when we assign the variable to a function then the function does not executes until we added try and except condition
# finally is used when we face any error in the program so that it executes properly
# finally is used to clean up the file and also to close the file when the file is open
# Dtabase connection mna gar koi error agya hai to us ko revoke kernai kai liay


