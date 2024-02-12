import os
from django.conf import settings

pizza_list = [
    {
        "name": "Focaccia",
        "ingredients": "Bread with italian olive oil and rosemary",
        "price": 6,
        "image": "pizzas/focaccia.jpg",
        "sold_out": False,
    },
    {
        "name": "Pizza Margherita",
        "ingredients": "Tomato and mozarella",
        "price": 10,
        "image": "pizzas/margherita.jpg",
        "sold_out": False,
    },
    {
        "name": "Pizza Spinaci",
        "ingredients": "Tomato, mozarella, spinach, and ricotta cheese",
        "price": 12,
        "image": "pizzas/spinaci.jpg",
        "sold_out": False,
    },
    {
        "name": "Pizza Funghi",
        "ingredients": "Tomato, mozarella, mushrooms, and onion",
        "price": 12,
        "image": "pizzas/funghi.jpg",
        "sold_out": False,
    },
    {
        "name": "Pizza Salamino",
        "ingredients": "Tomato, mozarella, and pepperoni",
        "price": 15,
        "image": "pizzas/salamino.jpg",
        "sold_out": True,
    },
    {
        "name": "Pizza Prosciutto",
        "ingredients": "Tomato, mozarella, ham, aragula, and burrata cheese",
        "price": 18,
        "image": "pizzas/prosciutto.jpg",
        "sold_out": False,
    },
]
