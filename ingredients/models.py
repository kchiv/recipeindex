from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IngredientCategory(models.Model):
    category_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category_name = models.CharField(max_length=400, unique=True, blank=False)

    class Meta:
        verbose_name_plural = 'ingredient categories'
    
    def __str__(self):
        return self.category_name

class Ingredient(models.Model):
    ingredient_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ingredient_name = models.CharField(max_length=400, unique=True, blank=False)
    ingredient_category = models.ManyToManyField(IngredientCategory, blank=True)

    def __str__(self):
        return self.ingredient_name