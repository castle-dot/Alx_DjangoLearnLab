# query_samples.py

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable to point to your settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Setup Django
django.setup()

# Now import your models
# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(f"Book: {book.title}, Author: {book.author.name}")

# Query 2: List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Book: {book.title}, Library: {library.name}")

# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library.name}: {librarian.name}")

# Example usage (you can call these functions to test them)
if __name__ == "__main__":
    print("Books by 'J.K. Rowling':")
    books_by_author('J.K. Rowling')  # Replace with an actual author name in your database

    print("\nBooks in 'Central Library':")
    books_in_library('Central Library')  # Replace with an actual library name in your database

    print("\nLibrarian for 'Central Library':")
    librarian_for_library('Central Library')  # Replace with an actual library name in your database
