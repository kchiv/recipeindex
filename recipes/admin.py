from django.contrib import admin
from .models import (
    Author,
    Publisher,
    Cuisine,
    Meal,
    Dish,
    Category,
    Size,
    Recipe
)

# Register your models here.

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Recipe)