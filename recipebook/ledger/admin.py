from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    fields = ['ingredient','recipe','quantity']

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ("name",)
    list_display = ("id","name",)
    list_filter = ("name",)

    inlines = [
            RecipeIngredientInline,
            ]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ("name",)
    list_display = ("id","name",)
    list_filter = ("name",)
    inlines = [
            RecipeIngredientInline,
            ]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ("quantity","ingredient","recipe",)
    list_filter = ("recipe","ingredient",)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
