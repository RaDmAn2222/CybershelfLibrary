from django.urls import path
from .views import contact, books, main, about, thank_you, authors_list, genres_list, genre_books, author_books

urlpatterns = [
    path('', main, name='main'),
    path('books/', books, name='books'),
    path('about/', about, name='about'),
    path('submit/', contact, name='contact'),
    path('thank_you/', thank_you, name='thank_you'),
    path('genres/', genres_list, name='genres_list'),
    path('authors/', authors_list, name='authors_list'),
    path('genres/<str:name>/', genre_books, name='genre_books'),
    path('authors/<str:name>', author_books, name='author_books'),
]
