from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request):
    """The home page for our Pizzeria"""
    return render(request, 'pizzeria_app/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')
    context = {'pizzas':pizzas}
    return render(request, 'pizzeria_app/pizzas.html', context)