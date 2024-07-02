from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200, null=True, blank=True)
    pdf_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title