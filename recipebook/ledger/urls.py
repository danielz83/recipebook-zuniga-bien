from django.urls import path
from .views import recipes_list, recipe_with_param

urlpatterns = [
        path('recipes/list/', recipes_list, name='recipes_list'),
        path('recipe/<int:num>/', recipe_with_param, name='recipe'),
        ]

appname = "ledger"
