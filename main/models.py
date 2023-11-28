from django.db import models


# Модель книги
class BookModel(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    year = models.IntegerField()
    ISBN = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
