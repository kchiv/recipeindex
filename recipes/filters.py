from django.db.models import Q
from django import forms
from dal import autocomplete
import django_filters
from .models import (
    Recipe, 
    Type,
    Author,
    Publisher,
    Cuisine,
    Category,
    Meal,
    Dish,
    Ingredient,
    Event
    )
from ingredients.models import Ingredient

def name_custom_filter(queryset, name, value):
        return Recipe.objects.filter(
            Q(recipe_name_custom__icontains=value) | 
            Q(recipe_name_title_tag__icontains=value) | 
            Q(recipe_name_h1__icontains=value)
        )

def filter_not_empty(queryset, name, value):
    # filter used to generate boolean logic for rte fields
    # to check whether blank or not
    if value == True:
        lookup = '__'.join([name, 'exact'])
        return queryset.exclude(**{lookup: ''})
    else:
        lookup = '__'.join([name, 'exact'])
        return queryset.filter(**{lookup: ''})

class RecipeFilter(django_filters.FilterSet):
    recipe_name_custom = django_filters.CharFilter(
        method=name_custom_filter,
        label='Recipe Name', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    recipe_rating = django_filters.LookupChoiceFilter(
        label='Rating',
        field_class=forms.DecimalField,
        lookup_choices=[
            ('exact', '='),
            ('gt', '>'),
            ('gte', '>='),
            ('lt', '<'),
            ('lte', '<='),
            ('isnull', '--')
        ]
    )
    recipe_author = django_filters.filters.ModelMultipleChoiceFilter(
        label='Author', 
        queryset=Author.objects.all(), 
        widget=autocomplete.ModelSelect2Multiple(url='recipes:author-autocomplete-filter'))
    recipe_publisher = django_filters.filters.ModelMultipleChoiceFilter(
        label='Publisher', 
        queryset=Publisher.objects.all(), 
        widget=autocomplete.ModelSelect2Multiple(url='recipes:publisher-autocomplete-filter'))
    recipe_type = django_filters.filters.ModelMultipleChoiceFilter(
        label='Publisher Type',
        field_name='recipe_publisher__publisher_type', 
        to_field_name='id', 
        queryset=Type.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='recipes:type-autocomplete-filter'))
    recipe_cuisine = django_filters.filters.ModelMultipleChoiceFilter(
        label='Cuisine', 
        queryset=Cuisine.objects.all(), 
        widget=autocomplete.ModelSelect2Multiple(url='recipes:cuisine-autocomplete-filter'))
    recipe_meal = django_filters.filters.ModelMultipleChoiceFilter(
        label='Meal', 
        queryset=Meal.objects.all(), 
        widget=autocomplete.ModelSelect2Multiple(url='recipes:meal-autocomplete-filter'))
    recipe_dish = django_filters.filters.ModelMultipleChoiceFilter(
        label='Dish', 
        queryset=Dish.objects.all(), 
        widget=autocomplete.ModelSelect2Multiple(url='recipes:dish-autocomplete-filter'))
    recipe_category = django_filters.filters.ModelMultipleChoiceFilter(
        label='Category', 
        queryset=Category.objects.all(), 
        widget=autocomplete.ModelSelect2Multiple(url='recipes:category-autocomplete-filter'))
    recipe_ingredients = django_filters.filters.ModelMultipleChoiceFilter(
        label='Ingredients', 
        queryset=Ingredient.objects.all(), 
        widget=autocomplete.ModelSelect2Multiple(url='ingredients:ingredient-autocomplete-filter'))
    recipe_event = django_filters.filters.ModelMultipleChoiceFilter(
        label='Event', 
        queryset=Event.objects.all(), 
        widget=autocomplete.ModelSelect2Multiple(url='recipes:event-autocomplete-filter'))
    recipe_time_amount = django_filters.LookupChoiceFilter(
        label='Time (Hours)',
        field_class=forms.DecimalField,
        lookup_choices=[
            ('exact', '='),
            ('gt', '>'),
            ('gte', '>='),
            ('lt', '<'),
            ('lte', '<='),
            ('isnull', '--')
        ]
    )
    recipe_created_date = django_filters.DateFromToRangeFilter()
    recipe_full_ingredients = django_filters.BooleanFilter(label='Full Ingredients Exist', method=filter_not_empty)
    recipe_full_steps = django_filters.BooleanFilter(label='Full Steps Exist', method=filter_not_empty)
    recipe_alterations = django_filters.BooleanFilter(label='Alterations Exist', method=filter_not_empty)
    recipe_notes = django_filters.BooleanFilter(label='Notes Exist', method=filter_not_empty)
    recipe_instantpot = django_filters.BooleanFilter(label='Instantpot Recipe')
    recipe_wayback_url = django_filters.BooleanFilter(label='Wayback URLs Exist', method=filter_not_empty)
    recipe_full_ingredients_search = django_filters.CharFilter(
        field_name='recipe_full_ingredients',
        lookup_expr='icontains',
        label='Search Full Ingredients', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    recipe_full_steps_search = django_filters.CharFilter(
        field_name='recipe_full_steps',
        lookup_expr='icontains',
        label='Search Full Steps', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    recipe_alterations_search = django_filters.CharFilter(
        field_name='recipe_alterations',
        lookup_expr='icontains',
        label='Search Alterations', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    recipe_notes_search = django_filters.CharFilter(
        field_name='recipe_notes',
        lookup_expr='icontains',
        label='Search Notes', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    # recipe_created_date = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year')
    # recipe_created_date__gt = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year__gt')
    # recipe_created_date__lt = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year__lt')

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
            'recipe_rating',
            'recipe_publisher', 
            'recipe_type',
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
            'recipe_created_date',
            'recipe_full_ingredients',
            ]

    # def __init__(self, *args, **kwargs):
    #     super(RecipeFilter, self).__init__(*args, **kwargs)
    #     self.filters['recipe_name_custom'].extra.update({'empty_label': 'Recipe Name'})
    
    @property
    def qs(self):
        parent = super().qs
        active_user = getattr(self.request, 'user', None)

        return parent.filter(recipe_user=active_user)