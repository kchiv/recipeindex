from django.shortcuts import render
from dal import autocomplete
from .models import Ingredient

# Create your views here.

class IngredientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Ingredient.objects.filter(ingredient_user=self.request.user)

        if self.q:
            qs = qs.filter(ingredient_name__icontains=self.q)
        
        return qs
    
    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'ingredient_user': self.request.user})