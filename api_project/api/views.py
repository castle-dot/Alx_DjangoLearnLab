from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book  # The model we are querying
from .serializers import BookSerializer  # The serializer we just created

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all Book objects
    serializer_class = BookSerializer