from django.shortcuts import render, redirect
from .models import Pizza, Topping
from .forms import CommentForm

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
    pizza_with_comments = pizza.comment_set.order_by('-date_added')
    context = {'pizza':pizza, 'pizza_with_toppings':pizza_with_toppings, 'pizza_with_comments':pizza_with_comments}
    return render(request, 'pizzeria_app/pizza.html', context)

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect('pizzeria_app:pizza', pizza_id=pizza_id)
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzeria_app/new_comment.html', context)