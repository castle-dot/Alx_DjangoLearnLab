from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book  # The model we are querying
from .serializers import BookSerializer  # The serializer we just created
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # This retrieves all books from the database
    serializer_class = BookSerializer  # This specifies the serializer to use for converting model instances to JSON and vice versa
    permission_classes = [IsAuthenticated]  # This ensures that only authenticated users can access this view

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all Book objects
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # This retrieves all books from the database
    serializer_class = BookSerializer  # This specifies the serializer to use for converting model instances to JSON and vice versa
    permission_classes = [IsAuthenticated]  # This ensures that only authenticated users can access this view