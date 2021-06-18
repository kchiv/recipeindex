from django.contrib import admin
from .models import IngredientCategory, Ingredient

# Register your models here.

admin.site.register(IngredientCategory)
admin.site.register(Ingredient)