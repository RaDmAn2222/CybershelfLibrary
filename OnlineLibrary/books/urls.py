from django.urls import path
from .views import contact, books, main, about, thank_you

urlpatterns = [
    path('', main, name='main'),
    path('books/', books, name='books'),
    path('about/', about, name='about'),
    path('submit/', contact, name='contact'),
    path('thank_you/', thank_you, name='thank_you'),
]
