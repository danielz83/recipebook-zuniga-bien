from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ("id","name",)
    list_filter = ("name",)

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ("id","name",)
    list_filter = ("name",)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ("quantity","ingredient","recipe",)
    list_filter = ("recipe","ingredient",)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
