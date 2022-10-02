from django.db import models

# Create your models here.
class Fooditem(models.Model):
    #Model for food items
    name = models.CharField(max_length=50)
    produsent = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)

    #numbers per 100g
    calories = models.DecimalField(decimal_places=2, max_digits=6, blank=True)
    protein = models.DecimalField(decimal_places=2, max_digits=6, blank=True)
    carbohydrates = models.DecimalField(decimal_places=2, max_digits=6, blank=True)
    fat = models.DecimalField(decimal_places=2, max_digits=6, blank=True)
    sugar = models.DecimalField(decimal_places=2, max_digits=6, blank=True)
    fibre = models.DecimalField(decimal_places=2, max_digits=6, blank=True)

    def __str__(self):
        return self.name
