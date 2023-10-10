from django.db import models


# Book data model
class Book(models.Model):
    title = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=64)
    genre = models.CharField(max_length=32, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
