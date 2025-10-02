from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Store the author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)  # Store the book title
    publication_year = models.IntegerField()  # Store the year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Link to the Author model

    def __str__(self):
        return self.title