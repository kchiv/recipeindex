import django_filters
from .models import Recipe
from ingredients.models import Ingredient

class RecipeFilter(django_filters.FilterSet):
    recipe_name_custom = django_filters.CharFilter(lookup_expr='icontains')

    recipe_created_date = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year')
    recipe_created_date__gt = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year__gt')
    recipe_created_date__lt = django_filters.NumberFilter(field_name='recipe_created_date', lookup_expr='year__lt')

    recipe_ingredients = django_filters.filters.ModelMultipleChoiceFilter(field_name='recipe_ingredients__ingredient_name', to_field_name='ingredient_name', queryset=Ingredient.objects.all())



    class Meta:
        model = Recipe
        fields = ['recipe_name_custom', 'recipe_created_date', 'recipe_ingredients']