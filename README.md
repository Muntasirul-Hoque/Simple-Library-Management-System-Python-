# Simple-Library-Management-System-Python-

A simple Python-based system to manage books in a library. Users can view, borrow, and return books, with error handling for invalid actions.

## Features
- **View All Books**: Displays all books in the library.
- **Borrow Book**: Borrow a book if available.
- **Return Book**: Return a borrowed book.
- **Error Handling**: Handles invalid book ID, borrowing already borrowed books, and returning books not borrowed.
- **Data Privacy**: Book attributes are protected to ensure privacy.

## Classes
### `Library`
- Manages the list of books with `entry_book()` to add books.

### `Book`
- Represents individual books with methods:
  - `borrow_book()`: Borrow a book.
  - `return_book()`: Return a book.
  - `view_book_info()`: View book details.
