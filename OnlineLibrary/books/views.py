from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author

def books(request):
    books = Book.objects.select_related('author').all()
    template = loader.get_template("books.html")
    context = {
        "books": books,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def info(request):
    template = loader.get_template('info.html')
    return HttpResponse(template.render())