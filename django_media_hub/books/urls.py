from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name = 'books_index'),
    path("catalog/", views.catalog, name = 'book_catalog'),
    path("books/<info>/", views.book_info, name = 'book_info'),
]