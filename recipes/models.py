from django.db import models
from ingredients.models import Ingredient

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=400, unique=True, blank=False)

class PublisherDomain(models.Model):
    domain_name = models.CharField(max_length=400, unique=True, blank=False)

class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=400, unique=True, blank=False)

class Meal(models.Model):
    meal_name = models.CharField(max_length=400, unique=True, blank=False)

class Dish(models.Model):
    dish_name = models.CharField(max_length=400, unique=True, blank=False)

class Category(models.Model):
    category_name = models.CharField(max_length=400, unique=True, blank=False)

class Recipe(models.Model):
    recipe_url = models.URLField(max_length=600, unique=True, blank=True)
    recipe_name_custom = models.CharField(max_length=500, unique=False, blank=False)
    recipe_name_title_tag = models.CharField(max_length=500, unique=False, blank=True)
    recipe_name_h1 = models.CharField(max_length=400, unique=False, blank=True)
    recipe_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    recipe_domain = models.ForeignKey(PublisherDomain, blank=True)
    recipe_alterations = models.CharField(max_length=400, unique=False, blank=True) # need to make this rich text edtor field
    recipe_notes = models.CharField(max_length=400, unique=False, blank=True) # need to make this rich text edtor field
    recipe_instantpot = models.BooleanField(default=False)
    recipe_author = models.ManyToManyField(Author, blank=True)
    recipe_cuisine = models.ManyToManyField(Cuisine, blank=True)
    recipe_meal = models.ManyToManyField(Meal, blank=True)
    recipe_dish = models.ManyToManyField(Dish, blank=True)
    recipe_category = models.ManyToManyField(Category, blank=True)
    recipe_ingredients = models.ManyToManyField(Ingredient, blank=True)