import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")  # change project name if needed
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """Query all books by a specific author"""
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


def list_books_in_library(library_name):
    """List all books in a library"""
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)
    return library.librarian


if __name__ == "__main__":
    # Examples
    print("Books by Author X:")
    for book in query_books_by_author("Author X"):
        print(book.title)

    print("\nBooks in Central Library:")
    for book in list_books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian of Central Library:")
    librarian = get_librarian_for_library("Central Library")
    print(librarian.name if librarian else "No librarian assigned")
