from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('books/', views.books, name='books'),
    path('about/', views.about, name='about'),
]