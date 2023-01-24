from django.forms import ModelForm
from .models import Fooditem,FoodEntry, Journal

class FoodForm(ModelForm):
    class Meta:
        model = Fooditem
        fields='__all__'

class FoodEntryForm(ModelForm):
    """ def __init__(self, user, *args, **kwargs):
        self.user = user
        super(FoodEntryForm, self).__init__(self, *args, **kwargs)
        self.fields['journal'].initial = Journal.objects.get(user=self.user)
 """
    class Meta:
        model = FoodEntry
        fields=['food', 'amount', 'date']
        

