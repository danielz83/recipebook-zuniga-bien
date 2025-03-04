from django.db import models

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

    class Meta:
        ordering = ['name']
        unique_together = ['name']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('recipe_detail',args=[str(self.name)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    class Meta:
        ordering = ['ingredient']
        unique_together = [['ingredient','recipe']]
