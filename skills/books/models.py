from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=120, verbose_name='Nombre')
    last_name = models.CharField(max_length=120, verbose_name='Apellido')
    birth_date = models.DateField(verbose_name='Fecha de Nacimiento')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')


    class Meta:
        db_table = 'authors'

class Book(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nombre')
    isbn = models.IntegerField(default=0, verbose_name='ISBN')
    publisher_date = models.DateField(verbose_name='Fecha de publicación')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, verbose_name='Author')

    class Meta:
        db_table = 'books'

