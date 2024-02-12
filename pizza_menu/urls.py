from django.urls import path
from . import views

urlpatterns = [
    path('pizza-list/', views.PizzaList.as_view(), name="pizza-list"),
]