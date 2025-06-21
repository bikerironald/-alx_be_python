# Objective: Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

# Task Description:
# Develop two Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

# library_system.py:
# Base Class - Book:

# Attributes: title (str) and author (str).
# Method: __init__(self, title, author) for initializing book attributes.
# Derived Classes - EBook and PrintBook:

# Both classes inherit from Book.
# EBook additional attribute: file_size (int).
# PrintBook additional attribute: page_count (int).
# Each derived class should have its own __init__ method that properly calls the base class __init__ while also initializing its unique attribute.
# Composition - Library:

# Attributes: books (a list to store instances of Book, EBook, and PrintBook).
# Methods:
# add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
# list_books(self): Prints details of each book in the library.
# main.py (Provided for Testing):
# This script tests the functionality of your classes in library_system.py by adding different types of books to a Library instance and listing them.

# from library_system import Book, EBook, PrintBook, Library

# def main():
#     # Create a Library instance
#     my_library = Library()

#     # Create instances of each type of book
#     classic_book = Book("Pride and Prejudice", "Jane Austen")
#     digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
#     paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

#     # Add books to the library
#     my_library.add_book(classic_book)
#     my_library.add_book(digital_novel)
#     my_library.add_book(paper_novel)

#     # List all books in the library
#     my_library.list_books()

# if __name__ == "__main__":
#     main()
# Expected Output:
# Your output should list the details of each book added to the library, reflecting the specific attributes of EBook and PrintBook, as well as the common attributes inherited from Book.

# Book: Pride and Prejudice by Jane Austen
# EBook: Snow Crash by Neal Stephenson, File Size: 500KB
# PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234


class Book:
    def __init__(self, title, author ):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"    
        
book1 = Book("Book: Pride and Prejudice", "Jane Austen")
print (book1)
        # print(f"Book: ", self.title, " by " , self.author) 
        # pass

class EBook(Book):
    def __init__(self, title, author, file_size ):
        super().__init__(title, author)
        self.file_size = file_size
        print(f"EBook: {title} by {author}, File Size: {file_size}KB")
        pass
        
        
class PrintBook(Book):
    def __init__(self, title, author, page_count ):
        super().__init__(title, author)
        self.page_count = page_count
        print(f"PrintBook: {self.title} by {self.author}, Page Count: {page_count}")
        pass


class Library():
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book) 

        if isinstance(book, EBook):
            self.books.append(book) 

        elif isinstance(book, PrintBook):
            self.books.append(book)      

        else:
            pass

    def list_books(self):
        for book in self.books:
            return book