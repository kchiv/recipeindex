from django.db import models

# Create your models here.

class IngredientCategory(models.Model):
    category_name = models.CharField(max_length=400, unique=True, blank=False)

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=400, unique=True, blank=False)
    ingredient_category = models.ManyToManyField(IngredientCategory, blank=True)