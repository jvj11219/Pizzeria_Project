from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for our Pizzeria"""
    return render(request, 'pizzeria_app/index.html')