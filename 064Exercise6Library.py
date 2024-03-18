"""
Write a Library class with no_of_books and books as two instance variables. 
Write a program to create a library from this Library class and show how you 
can print all books, add a book and get the number of books using different methods. 
Show that your program doesnt persist the books after the program is stopped!
"""

class Library:
    def __init__(self):
        self.number_of_books = 0
        self.books = []
    
    def add_books(self,books):
        self.books.append(books)
        print(f"You added {self.books[self.number_of_books]} in your library")
        self.number_of_books = self.number_of_books + 1

    def show_number_of_books(self):
        print(f"The number of books in your library are {self.number_of_books}")

    def list_books(self):
        for book in self.books:
            print(book)

l1 = Library()
l1.add_books("The Godfather")
l1.add_books("Anne Frank")
l1.add_books("The Metamorphosis")
l1.add_books("Animal Farm")
l1.list_books()
l1.show_number_of_books()