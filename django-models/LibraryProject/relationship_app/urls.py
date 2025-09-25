from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    # Define the URL pattern for the library detail page
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # Add any other views you need here
]
