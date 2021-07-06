from django import forms
import django_filters
from .models import (
    Recipe, 
    Type,
    Author
    )
from ingredients.models import Ingredient

class RecipeFilter(django_filters.FilterSet):
    recipe_name_custom = django_filters.CharFilter(lookup_expr='icontains', label='Recipe Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    recipe_author = django_filters.filters.ModelMultipleChoiceFilter(label='Author', queryset=Author.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    recipe_type = django_filters.filters.ModelMultipleChoiceFilter(
        field_name='recipe_publisher__publisher_type', 
        to_field_name='id', 
        queryset=Type.objects.all())
    recipe_created_date = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year')
    recipe_created_date__gt = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year__gt')
    recipe_created_date__lt = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year__lt')

    # ingredient_object = Ingredient.objects.all()
    # ingredient_list = []
    # for ingredient in ingredient_object:
    #     ingredient_list.append((ingredient.pk, ingredient.ingredient_name))
    # print(ingredient_list)
    # ingredient_tuple = tuple(ingredient_list)
    # print(ingredient_tuple)
    # recipe_ingredients = django_filters.TypedChoiceFilter(choices=ingredient_tuple)

    # recipe_ingredients = django_filters.filters.ModelMultipleChoiceFilter(field_name='recipe_ingredients__ingredient_name', to_field_name='ingredient_name', queryset=Ingredient.objects.all())


    class Meta:
        model = Recipe
        fields = [
            'recipe_name_custom', 
            'recipe_publisher', 
            'recipe_author',
            'recipe_cuisine',
            'recipe_meal',
            'recipe_dish',
            'recipe_category',
            'recipe_ingredients',
            'recipe_event',
            'recipe_calories',
            'recipe_protein',
            'recipe_difficulty',
            'recipe_time_amount',
            'recipe_priority',
            'recipe_created_date'
            ]

    # def __init__(self, *args, **kwargs):
    #     super(RecipeFilter, self).__init__(*args, **kwargs)
    #     self.filters['recipe_name_custom'].extra.update({'empty_label': 'Recipe Name'})
    
    @property
    def qs(self):
        parent = super().qs
        active_user = getattr(self.request, 'user', None)

        return parent.filter(recipe_user=active_user)