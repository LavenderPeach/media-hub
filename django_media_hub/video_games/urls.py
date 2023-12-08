from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name = 'video_games_index'),
    path("catalog/", views.catalog, name = 'video_games_catalog'),
    path("videogames/<info>/", views.video_game_info, name = 'video_game_info'),
]