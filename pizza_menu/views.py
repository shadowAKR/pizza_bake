from rest_framework.generics import ListAPIView

from .models import Pizza
from .serializers import PizzaListSerializer

# Create your views here.

class PizzaList(ListAPIView):
    serializer_class = PizzaListSerializer
    queryset = Pizza.objects.all()
