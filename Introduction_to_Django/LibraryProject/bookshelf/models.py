from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)          # VARCHAR(200)
    author = models.CharField(max_length=100)         # VARCHAR(100)
    publication_year = models.IntegerField()          # INT

    def __str__(self):
        return self.title
