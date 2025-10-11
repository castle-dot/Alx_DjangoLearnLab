from django.db import models


class Book(models.Model):
    # Field to store the title of the book
    title = models.CharField(max_length=100)
    
    # Field to store the author of the book
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} by {self.author}'
