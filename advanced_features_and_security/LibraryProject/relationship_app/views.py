from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
from django.shortcuts import get_object_or_404
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
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home or a dashboard page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def user_is_admin(user):
    return user.userprofile.role == 'Admin'
@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def user_is_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new book to the database
            return redirect('book_list')  # Redirect to the book list after adding
    else:
        form = BookForm()  # Create an empty form
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # Populate form with existing book data
        if form.is_valid():
            form.save()  # Save the changes to the book
            return redirect('book_list')  # Redirect to the book list after editing
    else:
        form = BookForm(instance=book)  # Create a form with the current book data
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()  # Delete the book from the database
        return redirect('book_list')  # Redirect to the book list after deleting
    return render(request, 'relationship_app/delete_book.html', {'book': book})