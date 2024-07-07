from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author
from django.core.paginator import Paginator
from django.db.models import Q

def books(request):
    query = request.GET.get('q')
    if query:
        books_list = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query)
        ).select_related('author')
    else:
        books_list = Book.objects.select_related('author').all()
        
    paginator = Paginator(books_list, 24)  # Show 24 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = loader.get_template("books.html")
    context = {
        "page_obj": page_obj,
        "query": query,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
