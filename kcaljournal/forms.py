from django import forms
from .models import Fooditem,FoodEntry, Journal

class DateInput(forms.DateInput):
    input_type = 'date'


class FoodForm(forms.ModelForm):
    class Meta:
        model = Fooditem
        fields='__all__'

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields=['food', 'amount', 'date']
        widgets = {
            'date': DateInput(),
        }
        

