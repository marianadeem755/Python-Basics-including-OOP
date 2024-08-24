dict={"The Lord of the Rings": 10,
      "Brave New World": 11,
      "War and Peace": 12,
      "The Catcher in the Rye": 13,
      "One Hundred Years of Solitude": 14,
      "To Kill a Mockingbird": 15,
      "The Great Gatsby": 16,
      "Crime and Punishment": 17,
      "Moby-Dick": 18,
      "Jane Eyre": 19,
      "The Hobbit": 20}
for key,value in dict.items():
    print(f"The value for key {key} is {value}")
if key==value:
    print("Here the key is equal to the value")
else:
    print("keys are not equal to value")


# write library class with number of books and books are two instance variables. 
# write a program to create a library from this library class 
# and show how you can print all books and a book and get the number of books using diffrent methods.
# show that your program does not persists the books after the program is stopped



class Library:
    def __init__(self):
        self.name_of_book="The Lord of the Rings"
        self.no_of_book=1
        def show(self):
            print(f"The name of book {self.name_of_book} has total in stock {self.no_of_book}")
class Library1(Library):
    def __init__(self):
        self.name_of_book="Brave New World"
        self.no_of_book=2
        print(f"The name of book {self.name_of_book} has total in stock {self.no_of_book}")
class Library2(Library):
    def __init__(self):
        self.name_of_book="War and Peace"
        self.no_of_book=3
        print(f"The name of book {self.name_of_book} has total in stock {self.no_of_book}")

class Library3(Library):
    def __init__(self):
        self.name_of_book="One Hundred Years of Solitude"
        self.no_of_book=4
        print(f"The name of book {self.name_of_book} has total in stock {self.no_of_book}")

class Library4(Library):
    def __init__(self):
        self.name_of_book="Brave New World"
        self.no_of_book=5
        print(f"The name of book {self.name_of_book} has total in stock {self.no_of_book}")
book=Library()
print(book.name_of_book, book.no_of_book)
book=Library1()
print(book.name_of_book, book.no_of_book)
book=Library2()
print(book.name_of_book, book.no_of_book)
book=Library3()
print(book.name_of_book, book.no_of_book)
book=Library4()
print(book.name_of_book, book.no_of_book)

        
class library:
    def __init__(self, books, no_of_books):
        self.books=books
        self.no_of_books=no_of_books
    def show(self):
        print("The are most popular book is The Lord of the Rings and left only 1 in stock")
        # print(f"The Book {self.books} has in total stock are {self.no_of_books}")
    def ret(self):
        if len(self.books)==self.no_of_books:
            print("Books are equal to the length of books")
        else: 
            print("Books are equal to the length of books")
class library1(library):
    def __init__(self, books, no_of_books):
        self.books=books
        self.no_of_books=no_of_books
        # print(f"The Book {self.books} has in total stock are {self.no_of_books}")
class library2(library):
    def __init__(self, books, no_of_books):
        self.books=books
        self.no_of_books=no_of_books
        # print(f"The Book {self.books} has in total stock are {self.no_of_books}")
class library3(library):
    def __init__(self, books, no_of_books):
        self.books=books
        self.no_of_books=no_of_books
        # print(f"The Book {self.books} has in total stock are {self.no_of_books}")
class library4(library):
    def __init__(self, books, no_of_books):
        self.books=books
        self.no_of_books=no_of_books
        # print(f"The Book {self.books} has in total stock are {self.no_of_books}")
books=["The Lord of the Rings", "Brave New World", "War and Peace", "he Catcher in the Rye", "One Hundred Years of Solitude"]
no_of_books=1,2,3,4,5
Library=library(books, no_of_books)
Library1=library1(books, no_of_books)
Library2=library2(books, no_of_books)
Library3=library3(books, no_of_books)
Library4=library4(books, no_of_books)
for i in range(len(books)):
    print(f"The Book is {books[i]} in stock is {no_of_books[i]}")
Library.show()
Library.ret()

