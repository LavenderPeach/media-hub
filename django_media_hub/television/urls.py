from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name = 'television_index'),
    path("catalog/", views.catalog, name = 'television_catalog'),
    path("television/<info>/", views.television_info, name='television_info')
]