from django.db import models
from django.urls import reverse
from accounts.models import Profile

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        unique_together = ['name']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('ingredient_detail',args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ['name']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('recipe_detail',args=[(self.id)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    class Meta:
        ordering = ['ingredient']
        unique_together = [['ingredient','recipe']]
