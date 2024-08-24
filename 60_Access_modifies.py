# Access Specifiers/Modifiers
# Access specifiers or access modifiers in python programming are used to limit the access of class variables 
# and class methods outside of class while implementing the concepts of inheritance.

# Let us see the each one of access specifiers in detail:

# Types of access specifiers
# Public access modifier
# Private access modifier
# Protected access modifier



class Employee:
    print("Hey, How are you!")
a=Employee()
a.emp1=56


# Public Modifiers
class Employee:
    print("Hey, How are you!")
    def __init__(self, name, occupation):
        self.name=name
        self.occ=occupation
        def show():
           print(f"Hey my name is {self.name} and my occupation is {self.occ}")
        show()


# a=Employee("Maria", "Datascience")
# print(a.name, a.occ)

# Private Modifiers
# cannot be accessed directly but can be accessed indirectly
# In this we do the name mangling(In Name Mangling we change the name of the private attribute)
class Employee:
    print("Hey, How are you!")
    def __init__(self, name, occupation):
        self.__name=name
        self.__occ=occupation
        def show():
           print(f"Hey my name is {self._Employee__name} and my occupation is {self._Employee__occ}")
        show()


a=Employee("Maria", "Datascience")
print(a._Employee__name, a._Employee__occ)
print(a.__dir__()) # dir aak method hai 
# # is sai hamai sarai attributes or methods dekhnai ko milain gai

# # protected Modifier
class student:
    def __init__(self):
        self.name="Maria Nadeem"
    def show(self):
        print(f"My name is {self.name}")
        return "code with harry"
class subject(student):
    print("I'm learning python now!")
obj=student()
print(obj.name)
print(obj.show())
print(dir(obj))
obj1=subject()
print(obj1.name)
print(dir(obj1))
print(obj1.show())

        
# Public Access Specifier in Python
# All the variables and methods (member functions) in python are by default public. 
# Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
class Myclass:
    def __init__(self, name, occupation):
        self.name=name
        self.occ=occupation
a=Myclass("Maria", "Datascience")
print(a.name, a.occ)


# Private Access Modifier
# By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class.
#  We cannot use private members outside of class.
# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. 
# However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__).
#  This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. 
# Code outside the class can still access these "private" variables and methods, 
# but it is generally understood that they should not be accessed or modified.
# Private members of a class cannot be accessed or inherited outside of class.
#  If we try to access or to inherit the properties of private members to child class (derived class). 
# Then it will show the error.

# Name mangling
# Name mangling in Python is a technique used to protect class-private and superclass-private attributes
#  from being accidentally overwritten by subclasses. 
# Names of class-private and superclass-private attributes are transformed 
# by the addition of a single leading underscore and a double leading underscore respectively.

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"
my_object = MyClass()
print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute        

# private Modifiers
class student:
    print("I'm learning code with herry course!")
    def __init__(self, name, occ):
        self.__name=name 
        self.__occ=occ
        def show():
           print(f"My name is {self._student__name} and I'm doing {self._student__occ}")
        show()
a=student("Maria Nadeem", "Datascience")
print(a._student__name, a._student__occ)



#Protected Access Modifier
# In object-oriented programming (OOP), the term "protected" is used to describe a member 
# (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. 
# In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_).
#  For example, if a class has a method called _my_method,
#  it is indicating that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention,
#  and does not actually provide any protection or restrict access to the member. 
# The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

class student:
    def __init__(self):
        self.name="Maria Nadeem"
    def _fun(self):
        return "We are learning Code with Herry python course"
class subject(student):
    print("Code with herry teaches python!")
a=student()
print(a.name)
print(a._fun())
print(a.__dir__())
b=subject()
print(b.name)
print(b._fun)
print(b.__dir__())






           
        




        

