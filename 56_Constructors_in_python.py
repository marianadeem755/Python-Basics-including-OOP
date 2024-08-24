# Constructors:
# A `constructor` is a special method in a class used to create and initialize an object of a class. 
# There are different types of constructors. Constructor is invoked automatically when an object of a class is created.
# A constructor is a unique function that gets called automatically when an object is created of a class.
#  The main purpose of a constructor is to initialize or assign values to the data members of that class. 
# It cannot return any value other than None.
# Types of Constructors in Python
# 1. Parameterized Constructor
# 2. Default Constructor
# Parameterized Constructor in Python
# When the constructor accepts arguments along with self, it is known as parameterized constructor.
# These arguments can be used inside the class to assign the values to the data members
# Default Constructor in Python
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
class Person:
    def __init__(self, n, occupation):
        self.name=n 
        self.occ=occupation
        print("Hey My name is Maria Nadeem")
    def info(self):
        print(f"Hey my name is {self.name} and I've completed my Bachelors and now I'm doing {self.occ}")
a=Person("Maria", "Datascience")
b=Person("shazia", "Housework")
a.info()
b.info()

class Housepreparation:
    def __init__(self, construction, all):
        print("I got my own house")
        self.cons=construction
        self.food=all
    def info(self):
        print(f"I got my own house and made of {self.cons} and it has {self.food} food")
a=Housepreparation("Wood", "pizza")
b=Housepreparation("Marbel", "Pasta")
a.info()
b.info()


       