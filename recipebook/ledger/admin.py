from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    fields = ['ingredient','recipe','quantity']

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ("name","author")
    list_display = ("id","name","author","created_on","updated_on")
    list_filter = ("name",)

    inlines = [
            RecipeIngredientInline,
            RecipeImageInline,
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
