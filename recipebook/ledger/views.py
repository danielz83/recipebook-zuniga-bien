from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Ingredient, RecipeImage
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
    recipe_ingredients = []

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        recipe_ingredient_form = RecipeIngredientForm()
        ctx['recipe_ingredient_form'] = recipe_ingredient_form
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        recipe = form.save(commit=False)
        recipe_ingredient_form = RecipeIngredientForm(self.request.POST)
        recipe_ingredient = recipe_ingredient_form.save(commit=False)
        recipe_ingredient.recipe = recipe
        recipe.save()
        recipe_ingredient.save()
        return super().form_valid(form)

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

class RecipeAddIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'
    template_name = 'ledger/recipe_add_ingredient.html'

    def get_success_url(self):
        return ''
