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
    date_created = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def get_food(self, date):
        #returns foodentry objects
        return FoodEntry.objects.filter(journal=self, date=date)

    def get_date_created(self):
        return self.date_created

    def calculate_nutrition(self, date):
        #calculates the total nutrition for a given date, returns a list of the totals
        #e.g [calories, protein, carbohydrates, fat, sugar, fibre]
        totals = [0,0,0,0,0,0]
        food_entries = list(self.get_food(date))
        nutritional_values = FoodEntry.list_food(food_entries)

        for i in nutritional_values:
            for j in range(2,8):
                totals[j - 2] += float(i[j])
        return totals


    
class FoodEntry(models.Model):
    #a specific entry in a Journal object, is essentially a FoodItem object with a specified amount.
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT)
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

    def list_food(entries):
        ###
        # takes a dictionary of food entry objects as keys and a dictionary of nutritional values as values 
        # returns a list where the first two elements is food name and amount and then 
        # next 6 elements are nutritional values. this repeats for all entries. 
        output = []
        for i in entries:
            nutritional_values = i.get_nutrition()
            output.extend([[str(i.food), 
            i.amount,
            nutritional_values['calories'],
            nutritional_values['protein'],
            nutritional_values['carbohydrates'],
            nutritional_values['fat'], 
            nutritional_values['sugar'], 
            nutritional_values['fibre']]])
        
        return output