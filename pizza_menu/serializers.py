from rest_framework.serializers import ModelSerializer

from .models import Pizza

class PizzaListSerializer(ModelSerializer):
    
    class Meta:
        model = Pizza
        fields = "__all__"
    