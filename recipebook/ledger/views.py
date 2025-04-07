from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Ingredient, RecipeImage, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm

# Create your views here.

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'

class RecipeAddView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'ledger/recipe_add.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recipe_ingredient_form'] = RecipeIngredientForm()
        ctx['ingredient_form'] = IngredientForm()
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class IngredientAddView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ledger/recipe_add.html'

    def get_success_url(self):
        return reverse("recipes_list")

class RecipeIngredientAddView(LoginRequiredMixin, CreateView):
    model = RecipeIngredient
    form_class = RecipeIngredientForm
    template_name = 'ledger/recipe_add.html'

class RecipeImageAddView(LoginRequiredMixin, CreateView):
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


class RecipeImageAddView(LoginRequiredMixin, CreateView):
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

