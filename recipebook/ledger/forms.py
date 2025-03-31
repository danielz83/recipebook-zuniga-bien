from django import forms
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
