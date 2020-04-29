from django.urls import path
from . import views

app_name = 'pizzeria_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas', views.pizzas, name='pizzas'),
]