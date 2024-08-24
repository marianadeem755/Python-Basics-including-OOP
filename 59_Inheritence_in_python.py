#Inheritance in python
#When a class derives from another class. 
# The child class will inherit all the public and protected properties and methods from the parent class.
#  In addition, it can have its own properties and methods,this is called as inheritance.
# Python Inheritance Syntax
# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#  Body of derived class

# Types of inheritance:
# Single inheritance
# Multiple inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance

# correct Method but not inheritence as the inheritence includes the extend of one class and create new class
class employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def showdemand(self):
        print(f"Id {self.id} employee name is {self.name}")
class Maneger:
    def __init__(self, name, language):
        self.name=name
        self.language=language
    def showlanguage(self):
        print(f"{self.name} teaches {self.language}")
a=employee("Maria", "212")
b=employee("shazia", "242")
c=Maneger("Maria Nadeem", "Python")
d=Maneger("Shazia Nadeem", "Lotus")
a.showdemand()
b.showdemand()
c.showlanguage()
d.showlanguage()
        

class employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def showdemand(self):
        print(f"Id {self.id} employee name is {self.name}")
class Maneger(employee):
    def showlanguage(self):
        print(f"Id {self.id} employee name is {self.name}")
        print("Python is great and essential programing language")
a=employee("Maria", "212")
b=employee("shazia", "242")
c=Maneger("Maria", "45")
d=Maneger("Shazia", "32")
a.showdemand()
b.showdemand()
c.showlanguage()
d.showlanguage()
        