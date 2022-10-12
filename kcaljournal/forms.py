from django.forms import ModelForm
from .models import Fooditem

class FoodForm(ModelForm):
    class Meta:
        model = Fooditem
        fields='__all__'

    