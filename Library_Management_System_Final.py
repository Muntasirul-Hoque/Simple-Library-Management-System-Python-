# -- Library Class
class Library:
    book_list = []

    def entry_book(self, book):
        Library.book_list.append(book)
        print(f"Book '{book._title}' added to the library.")

# -- Book Class
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = availability

    # -- Borrow
    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"'{self._title}' borrowed successfully.")
        else:
            print(f"'{self._title}' is already borrowed.")

    # -- Return
    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"'{self._title}' returned  successfully.")
        else:
            print(f"'{self._title}' is not borrowed.")

    # -- View Info
    def view_book_info(self):
        availability_status = "Available" if self._availability else "Not Available"
        print(f"Book ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Status: {availability_status}")

# -- Input
library = Library()
book1 = Book(101, "Kopa Phytron", "Muntasirul")
book2 = Book(102, "Academic + Phitron = *-*", "Hoque")
book3 = Book(103, "CSE = Computer Science EEE", "Alvi")

library.entry_book(book1)
library.entry_book(book2)
library.entry_book(book3)

# -- Menu System
def menu():
    while True:
        print("\nMenu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        
        try:
            n = int(input("Enter your choice: "))
            
            if n == 1:
                if Library.book_list:
                    for book in Library.book_list:
                        book.view_book_info()
                else:
                    print("No books in the library.")
            
            elif n == 2:
                book_id = int(input("Enter the Book ID to borrow: "))
                found = False
                for book in Library.book_list:
                    if book._book_id == book_id:
                        book.borrow_book()
                        found = True
                        break
                if not found:
                    print("Invalid Book ID.")
            
            elif n == 3:
                book_id = int(input("Enter the Book ID to return: "))
                found = False
                for book in Library.book_list:
                    if book._book_id == book_id:
                        book.return_book()
                        found = True
                        break
                if not found:
                    print("Invalid Book ID.")
            
            elif n == 4:
                print("Exiting the system...")
                break
            
            else:
                print("Invalid choice. Please enter a valid option.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

menu()
