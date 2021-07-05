import django_filters
from .models import Recipe
from ingredients.models import Ingredient

class RecipeFilter(django_filters.FilterSet):
    recipe_name_custom = django_filters.CharFilter(lookup_expr='icontains')
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
            'recipe_created_date', 
            'recipe_cuisine',
            'recipe_meal',
            'recipe_dish',
            'recipe_category',
            'recipe_ingredients',
            'recipe_calories',
            'recipe_protein'
            ]