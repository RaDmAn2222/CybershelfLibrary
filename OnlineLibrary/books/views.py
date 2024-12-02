from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author, Genre
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt


def books(request):
    query = request.GET.get('q')
    if query:
        # Updated to include search by genre name
        books_list = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(genre__name__icontains=query)
        ).select_related('author').prefetch_related('genre').distinct()
    else:
        books_list = Book.objects.select_related('author').prefetch_related('genre').all()

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


@csrf_exempt
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            full_message = f"Message from: {email}\n\n{message}"
            send_mail(
                "New Contact Us Message from CyberShelfLibrary",
                full_message,
                settings.DEFAULT_FROM_EMAIL,  # Use the default from email
                [settings.SUPPORT_EMAIL],  # This should be a list
                fail_silently=False,
            )
            return redirect("thank_you")
    else:
        form = ContactForm()

    template = loader.get_template("main.html")
    context = {
        "form": form,
    }
    return HttpResponse(template.render(context, request))


def thank_you(request):
    template = loader.get_template("thank_you.html")
    return HttpResponse(template.render())


def authors_list(request):
    authors = Author.objects.all()
    unique_authors = {author.name: author for author in authors}.values()
    template = loader.get_template("authors.html")
    context = {
        'authors': unique_authors
    }
    return HttpResponse(template.render(context, request))


def genres_list(request):
    genres = Genre.objects.all()
    template = loader.get_template("genres.html")
    context = {
        'genres': genres
    }
    return HttpResponse(template.render(context, request))


def genre_books(request, name):
    genre = get_object_or_404(Genre, name=name)
    books = Book.objects.filter(genre=genre).select_related('author').prefetch_related('genre')
    template = loader.get_template("genre_books.html")
    paginator = Paginator(books, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'genre': genre,
    }
    return HttpResponse(template.render(context, request))


def author_books(request, name):
    authors = Author.objects.filter(name=name)
    books = Book.objects.filter(author__in=authors).select_related('author').prefetch_related('genre')
    template = loader.get_template("author_books.html")
    paginator = Paginator(books, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author': authors,
    }
    return HttpResponse(template.render(context, request))