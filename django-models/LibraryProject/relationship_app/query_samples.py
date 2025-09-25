# query_samples.py

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable to the correct path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Setup Django
django.setup()

# Now import your models
from relationship_app.models import Author, Book, Library, Librarian

# Function to get all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            print(f"Book: {book.title}, Author: {book.author.name}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

# Function to list all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"Book: {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

# Function to retrieve the librarian for a specific library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for the library {library_name}")

if __name__ == "__main__":
    # Example usage
    print("Books by 'J.K. Rowling':")
    books_by_author('J.K. Rowling')

    print("\nBooks in 'Central Library':")
    books_in_library('Central Library')

    print("\nLibrarian for 'Central Library':")
    librarian_for_library('Central Library')
