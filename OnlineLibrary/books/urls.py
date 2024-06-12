from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name="books"),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
]