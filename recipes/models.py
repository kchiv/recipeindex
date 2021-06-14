from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name_custom = models.CharField(max_length=400, unique=False, blank=False)
    recipe_name_title_tag = models.CharField(max_length=400, unique=False, blank=False)
    recipe_name_h1 = models.CharField(max_length=400, unique=False, blank=False)
    rating = models.models.DecimalField(max_digits=3, decimal_places=1)