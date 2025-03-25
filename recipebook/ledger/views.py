from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recipe, RecipeIngredient, Ingredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RecipeListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Recipe.objects.filter(author__user=self.request.user)
    template_name = 'ledger/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'

