from django.urls import path
from . import views 
from .views import list_books, LibraryDetailView # Import views from the current app

# relationship_app/urls.py

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # URL pattern for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for library details
]

