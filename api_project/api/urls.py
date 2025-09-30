# api/urls.py
from django.urls import path, include
from .views import BookList  # Import the BookList view
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Import the BookViewSet
from rest_framework.authtoken.views import obtain_auth_token    

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Endpoint to list all books
    path('', include(router.urls)),  # Include the router URLs
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),  # Endpoint for obtaining auth tokens
]