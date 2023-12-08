from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "books/index.html")

def catalog(request):
    pass

def book_info(request):
    pass