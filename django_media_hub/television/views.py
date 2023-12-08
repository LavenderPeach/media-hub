from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "television/index.html")

def catalog(request):
    pass

def television_info(request):
    pass