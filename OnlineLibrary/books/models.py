from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True, default=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    pdf_url = models.URLField(max_length=1000, null=True, blank=True)
    genre = models.ManyToManyField(Genre, through='Book_Genre')  # Link to the through model

    def __str__(self):
        return self.title

class Book_Genre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} - {self.genre.name}"
