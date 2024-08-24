class Library:
    def __init__(self):
        self.nobooks=0
        self.books=[]
    def addbooks(self, books):
        self.books.append(books)
        self.nobooks=len(self.books)
    def showinfo(self):
        print(f"There are total no of books {self.nobooks}. The names of the books are")
        for books in self.books:
            print(f"The Books names are {books}")
library=Library()
library.addbooks("Harry potter")
library.addbooks("Harry potter2")
library.addbooks("Harry potter3")
library.showinfo()


        