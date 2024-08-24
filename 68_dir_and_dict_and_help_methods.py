l=[3,4,5,78,90.23]
print(dir(l))
print("---------------------------------------------------------------------------------------------------")
print(dir(l.__add__))

t=(3,4,5,78,90.23)
print(dir(t))
print("---------------------------------------------------------------------------------------------------")
print(dir(t.__add__))

class Person():
    def __init__(self, name, fathername, salary):
      self.name=name
      self.fathername=fathername
      self.salary=salary
a=Person("Maria", "Nadeem", 50000)
print(a.name, a.fathername, a.salary)
print('--------------------------------------------------------------------------------')
print(a.__dict__)
print('--------------------------------------------------------------------------------')
print(help(a))