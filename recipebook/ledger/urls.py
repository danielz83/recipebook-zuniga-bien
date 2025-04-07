from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeAddView, RecipeImageAddView, IngredientAddView, RecipeIngredientAddView

urlpatterns = [
        path('recipes/list/', RecipeListView.as_view(), name='recipes_list'),
        path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
        path('recipe/add/', RecipeAddView.as_view(), name='recipe_add'),
        path('recipe/<int:pk>/add_image/', RecipeImageAddView.as_view(), name='recipe_add_image'),
        path('recipes/add_ingredient/', IngredientAddView.as_view(), name='recipe_add_ingredient'),
        path('recipes/add_recipe_ingredient/', RecipeIngredientAddView.as_view(), name='recipe_add_recipe_ingredient'),
        ]

appname = "ledger"
