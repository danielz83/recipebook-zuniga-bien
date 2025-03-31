from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeAddView, RecipeAddImageView, RecipeAddIngredientView
urlpatterns = [
        path('recipes/list/', RecipeListView.as_view(), name='recipes_list'),
        path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
        path('recipe/add/', RecipeAddView.as_view(), name='recipe_add'),
        path('recipe/<int:pk>/add_image', RecipeAddImageView.as_view(), name='recipe_add_image'),
        path('recipes/add_ingredient', RecipeAddIngredientView.as_view(), name='recipe_add_ingredient'),
        ]

appname = "ledger"
