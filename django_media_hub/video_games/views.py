from django.shortcuts import render

# Create your views here.


def starting_page(request):
    return render(request, "videogames/index.html")

def catalog(request):
    pass

def video_game_info(request):
    pass