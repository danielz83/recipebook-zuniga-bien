from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recipe, RecipeIngredient, Ingredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'

