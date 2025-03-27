from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'

class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["name","author"]
    template_name = 'ledger/recipe_add.html'

class RecipeAddImageView(LoginRequiredMixin, CreateView): 
    model = RecipeImage
    fields = ["image","description"]
    template_name = 'ledger/recipe_add_image.html'

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["recipe"] = Recipe.objects.get(pk=self.kwargs["pk"])
        return ctx

    def get_success_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.kwargs["pk"]})
