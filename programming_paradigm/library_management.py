# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Store the author's name
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        # Return the string in the format "Title by Author"
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Sorry, {title} is not available.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"{title} was not checked out.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)  # Will automatically call the __str__ method of the Book class
        else:
            print("No books are currently available.")
