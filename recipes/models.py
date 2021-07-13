from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField
from ingredients.models import Ingredient
from image.models import ImageFile

# Create your models here.

class Type(models.Model):
    type_name = models.CharField(max_length=400, unique=True, blank=False)

    def __str__(self):
        return self.type_name

class Author(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    author_name = models.CharField(max_length=400, unique=False, blank=False)

    def __str__(self):
        return self.author_name

class Publisher(models.Model):
    publisher_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    publisher_name = models.CharField(max_length=400, unique=False, blank=False)
    publisher_type = models.ForeignKey(Type, blank=True, on_delete=models.SET_NULL, null=True)
    domain_name = models.CharField(max_length=400, unique=False, blank=True)
    channel_url = models.URLField(max_length=600, blank=True)
    ingredients_scr_element = models.CharField(
        max_length=500, 
        unique=False, 
        blank=True, 
        verbose_name='ingredients scraped element')
    ingredients_scr_attr = models.CharField(
        max_length=500, 
        unique=False, 
        blank=True,
        verbose_name='ingredients scraped attribute')
    ingredients_scr_value = models.CharField(
        max_length=500, 
        unique=False, 
        blank=True,
        verbose_name='ingredients scraped value')
    directions_scr_element = models.CharField(
        max_length=500, 
        unique=False, 
        blank=True,
        verbose_name='directions scraped element')
    directions_scr_attr = models.CharField(
        max_length=500, 
        unique=False, 
        blank=True,
        verbose_name='directions scraped attribute')
    directions_scr_value = models.CharField(
        max_length=500, 
        unique=False, 
        blank=True,
        verbose_name='directions scraped value')

    def get_absolute_url(self):
        return reverse('recipes:publisher_detail', kwargs={'publisher_id': self.pk})

    def __str__(self):
        return self.publisher_name

class Cuisine(models.Model):
    cuisine_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    cuisine_name = models.CharField(max_length=400, unique=False, blank=False)

    def __str__(self):
        return self.cuisine_name

class Meal(models.Model):
    meal_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    meal_name = models.CharField(max_length=400, unique=False, blank=False)

    def __str__(self):
        return self.meal_name

class Dish(models.Model):
    dish_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dish_name = models.CharField(max_length=400, unique=False, blank=False)

    class Meta:
        verbose_name_plural = 'dishes'

    def __str__(self):
        return self.dish_name

class Category(models.Model):
    category_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category_name = models.CharField(max_length=400, unique=False, blank=False)

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
    event_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    event_name = models.CharField(max_length=400, unique=False, blank=False)

    def __str__(self):
        return self.event_name

class Recipe(models.Model):
    recipe_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    recipe_url = models.URLField(max_length=600, unique=False, blank=True)
    recipe_name_custom = models.CharField(
        max_length=500, 
        unique=False, 
        blank=False,
        verbose_name='recipe name')
    recipe_name_title_tag = models.CharField(
        max_length=500, 
        unique=False, 
        blank=True,
        verbose_name='title tag')
    recipe_name_h1 = models.CharField(
        max_length=400, 
        unique=False, 
        blank=True,
        verbose_name='h1')
    recipe_rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        blank=True, 
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
        verbose_name='rating'
    )
    recipe_publisher = models.ManyToManyField(Publisher, blank=True, verbose_name='publisher')
    recipe_full_ingredients = RichTextField('ingredients list', blank=True)
    recipe_full_steps = RichTextField('directions', blank=True)
    recipe_alterations = RichTextField('alterations', blank=True)
    recipe_notes = RichTextField('notes', blank=True)
    recipe_instantpot = models.BooleanField(default=False, verbose_name='instantpot required')
    recipe_author = models.ManyToManyField(Author, blank=True, verbose_name='author')
    recipe_cuisine = models.ManyToManyField(Cuisine, blank=True, verbose_name='cuisine')
    recipe_meal = models.ManyToManyField(Meal, blank=True, verbose_name='meal')
    recipe_dish = models.ManyToManyField(Dish, blank=True, verbose_name='dish')
    recipe_category = models.ManyToManyField(Category, blank=True, verbose_name='category')
    recipe_ingredients = models.ManyToManyField(Ingredient, blank=True, verbose_name='ingredients')
    recipe_created_date = models.DateTimeField(
        default=datetime.now().strftime("%Y-%m-%d"), 
        verbose_name='created date')
    recipe_calories = models.ForeignKey(
        Size, 
        blank=True, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='recipe_calories_size',
        verbose_name='calorie amount')
    recipe_protein = models.ForeignKey(
        Size, 
        blank=True, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='recipe_protein_size',
        verbose_name='protein amount')
    recipe_difficulty = models.ForeignKey(
        Size, 
        blank=True, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='recipe_difficulty_size',
        verbose_name='difficulty')
    recipe_time = models.ForeignKey(
        Size, 
        blank=True, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='recipe_time_size',
        verbose_name='time required')
    recipe_time_amount = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        blank=True, 
        null=True,
        verbose_name='time amount')
    recipe_priority = models.ForeignKey(
        Size, 
        blank=True, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='recipe_priority_size',
        verbose_name='priority')
    recipe_event = models.ManyToManyField(Event, blank=True, verbose_name='event')
    recipe_wayback_url = models.URLField(max_length=600, blank=True, verbose_name='wayback url')
    recipe_related_link_1 = models.URLField(max_length=600, blank=True, verbose_name='related link #1')
    recipe_related_link_2 = models.URLField(max_length=600, blank=True, verbose_name='related link #2')
    recipe_related_link_3 = models.URLField(max_length=600, blank=True, verbose_name='related link #3')
    recipe_file_storage = models.ManyToManyField(ImageFile, blank=True, verbose_name='files')

    def __str__(self):
        return self.recipe_name_custom
    
    def get_absolute_url(self):
        return reverse('recipes:recipe_detail', kwargs={'recipe_id': self.pk})