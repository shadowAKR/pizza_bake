from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=500)
    ingredients = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.name
