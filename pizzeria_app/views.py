from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.

def index(request):
    """The home page for our Pizzeria"""
    return render(request, 'pizzeria_app/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')
    context = {'pizzas':pizzas}
    return render(request, 'pizzeria_app/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    pizza_with_toppings = pizza.topping_set.order_by('topping_name')
    context = {'pizza':pizza, 'pizza_with_toppings':pizza_with_toppings}
    return render(request, 'pizzeria_app/pizza.html', context)