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
            print(f"'{self._title}' has been successfully borrowed.")
        else:
            print(f"'{self._title}' is already borrowed.")

    # -- Return
    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"'{self._title}' has been successfully returned.")
        else:
            print(f"'{self._title}' is not borrowed, so it cannot be returned.")

    # -- Info
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
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                if Library.book_list:
                    for book in Library.book_list:
                        book.view_book_info()
                else:
                    print("No books in the library.")
            
            elif choice == 2:
                book_id = int(input("Enter the Book ID to borrow: "))
                found = False
                for book in Library.book_list:
                    if book._book_id == book_id:
                        book.borrow_book()
                        found = True
                        break
                if not found:
                    print("Invalid Book ID.")
            
            elif choice == 3:
                book_id = int(input("Enter the Book ID to return: "))
                found = False
                for book in Library.book_list:
                    if book._book_id == book_id:
                        book.return_book()
                        found = True
                        break
                if not found:
                    print("Invalid Book ID.")
            
            elif choice == 4:
                print("Exiting the system...")
                break  # Exit the loop
            
            else:
                print("Invalid choice. Please enter a valid option.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

menu()