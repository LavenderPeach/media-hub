from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name = 'movies_index'),
    path("catalog/", views.catalog, name = 'movies_catalog'),
    path("movies/<info>/", views.film_info, name='movies_info')

]