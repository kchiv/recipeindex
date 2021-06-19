from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from ckeditor.fields import RichTextField
from ingredients.models import Ingredient

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=400, unique=True, blank=False)

    def __str__(self):
        return self.author_name

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=400, unique=True, blank=False)
    domain_name = models.CharField(max_length=400, unique=True, blank=False)

    def __str__(self):
        return self.publisher_name

class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=400, unique=True, blank=False)

    def __str__(self):
        return self.cuisine_name

class Meal(models.Model):
    meal_name = models.CharField(max_length=400, unique=True, blank=False)

    def __str__(self):
        return self.meal_name

class Dish(models.Model):
    dish_name = models.CharField(max_length=400, unique=True, blank=False)

    class Meta:
        verbose_name_plural = 'dishes'

    def __str__(self):
        return self.dish_name

class Category(models.Model):
    category_name = models.CharField(max_length=400, unique=True, blank=False)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

class Size(models.Model):
    size_name = models.CharField(max_length=400, unique=True, blank=False)
    size_order = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return self.size_name

class Event(models.Model):
    event_name = models.CharField(max_length=400, unique=True, blank=False)

    def __str__(self):
        return self.event_name

class Recipe(models.Model):
    recipe_url = models.URLField(max_length=600, unique=True, blank=True)
    recipe_name_custom = models.CharField(max_length=500, unique=False, blank=False)
    recipe_name_title_tag = models.CharField(max_length=500, unique=False, blank=True)
    recipe_name_h1 = models.CharField(max_length=400, unique=False, blank=True)
    recipe_rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        blank=True, 
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    recipe_publisher = models.ForeignKey(Publisher, blank=True, on_delete=models.SET_NULL, null=True)
    recipe_alterations = RichTextField('Recipe alterations', blank=True)
    recipe_notes = RichTextField('Recipe notes', blank=True)
    recipe_instantpot = models.BooleanField(default=False)
    recipe_author = models.ManyToManyField(Author, blank=True)
    recipe_cuisine = models.ManyToManyField(Cuisine, blank=True)
    recipe_meal = models.ManyToManyField(Meal, blank=True)
    recipe_dish = models.ManyToManyField(Dish, blank=True)
    recipe_category = models.ManyToManyField(Category, blank=True)
    recipe_ingredients = models.ManyToManyField(Ingredient, blank=True)
    recipe_created_date = models.DateTimeField(default=timezone.now)
    recipe_calories = models.ForeignKey(Size, blank=True, on_delete=models.SET_NULL, null=True, related_name='recipe_calories_size')
    recipe_protein = models.ForeignKey(Size, blank=True, on_delete=models.SET_NULL, null=True, related_name='recipe_protein_size')
    recipe_difficulty = models.ForeignKey(Size, blank=True, on_delete=models.SET_NULL, null=True, related_name='recipe_difficulty_size')
    recipe_time = models.ForeignKey(Size, blank=True, on_delete=models.SET_NULL, null=True, related_name='recipe_time_size')
    recipe_time_amount = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    recipe_priority = models.ForeignKey(Size, blank=True, on_delete=models.SET_NULL, null=True, related_name='recipe_priority_size')
    recipe_event = models.ForeignKey(Event, blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.recipe_name_custom