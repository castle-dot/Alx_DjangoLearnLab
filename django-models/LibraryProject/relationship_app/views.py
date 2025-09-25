from django.shortcuts import render


from relationship_app.models import Book
from django.views.generic.detail import DetailView
from relationship_app.models import Library
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template for rendering
    context_object_name = 'library'  # This will be used in the template

    def get_queryset(self):
        # Optionally, you can filter libraries if needed
        return Library.objects.all()

def list_books(request):
    # Get all books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
