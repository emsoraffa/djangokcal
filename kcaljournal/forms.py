from django.forms import DateInput, ModelForm
from .models import Fooditem,FoodEntry, Journal

class FoodForm(ModelForm):
    class Meta:
        model = Fooditem
        fields='__all__'

class FoodEntryForm(ModelForm):
    class Meta:
        model = FoodEntry
        fields=['food', 'amount', 'date']
        widgets = {
            'date': DateInput(),
        }
        

