from django.urls import path
from . import views 
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView  

# relationship_app/urls.py

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # URL pattern for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]

