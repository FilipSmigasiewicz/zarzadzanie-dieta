from django import forms
from .models import Meal, DietPlan

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'image', 'calories', 'protein', 'carbohydrates', 'fat', 'recipe']
        labels = {
            'name': 'Nazwa',
            'image': 'Obraz',
            'calories': 'Kalorie',
            'protein': 'Białko',
            'carbohydrates': 'Węglowodany',
            'fat': 'Tłuszcz',
            'recipe': 'Przepis',  
        }


class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['name', 'breakfast', 'lunch', 'dinner']
        labels = {
            'name': 'Nazwa',
            'breakfast': 'Śniadanie',
            'lunch': 'Obiad',
            'dinner': 'Kolacja',
        }
