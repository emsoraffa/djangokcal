from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fooditem(models.Model):
    #Model for food items
    name = models.CharField(max_length=50)
    producer = models.CharField(max_length=50, blank=True)
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

class Journal(models.Model):
    #Journal object unique to a user. Contains a list of Fooditem objects,
    #needs: date, foods, calories
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50, blank=True)
    def get_food(self, date):
        return FoodEntry.objects.filter(journal=self, date=date)

    
class FoodEntry(models.Model):
    #a specific entry in a Journal object, is essentially a FoodItem object with a specified amount.
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    food = models.ForeignKey(Fooditem, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=6, blank=True)
    date = models.DateField()

    def get_nutrition(self):
        #returns a dictionary with each nutritional value (based on the FoodItem object) multiplied by the amount
        nutrition = {
        'calories' : self.food.calories * (self.amount/100),
        'protein' : self.food.protein * (self.amount/100),
        'carbohydrates' : self.food.carbohydrates * (self.amount/100),
        'fat' : self.food.fat * (self.amount/100),
        'sugar' : self.food.sugar * (self.amount/100),
        'fibre' : self.food.fibre * (self.amount/100),
        }
        return nutrition

