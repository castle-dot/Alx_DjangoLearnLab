from rest_framework import serializers
from .models import Book  # Assuming the Book model is defined in api/models.py

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # The model we're serializing
        fields = '__all__'  # Include all fields from the Book model
