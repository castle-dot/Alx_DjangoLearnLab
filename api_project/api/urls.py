# api/urls.py
from django.urls import path
from .views import BookList  # Import the BookList view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Endpoint to list all books
]
