from django import forms
from django.urls import reverse_lazy
from dal import autocomplete
from django_addanother.widgets import AddAnotherWidgetWrapper
from . import models

class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['recipe_instantpot'].widget.attrs = {'class': 'form-check-input'}
        self.fields['recipe_created_date'].widget.attrs = {'id': 'my_date_picker', 'class': 'form-control'}

    class Meta:
        model = models.Recipe
        fields = '__all__'
        exclude = ['recipe_user']
        widgets = {
            'recipe_author': autocomplete.ModelSelect2Multiple(url='recipes:author-autocomplete'),
            'recipe_publisher': autocomplete.ModelSelect2Multiple(url='recipes:publisher-autocomplete'),
            'recipe_cuisine': autocomplete.ModelSelect2Multiple(url='recipes:cuisine-autocomplete'),
            'recipe_meal': autocomplete.ModelSelect2Multiple(url='recipes:meal-autocomplete'),
            'recipe_dish': autocomplete.ModelSelect2Multiple(url='recipes:dish-autocomplete'),
            'recipe_category': autocomplete.ModelSelect2Multiple(url='recipes:category-autocomplete'),
            'recipe_event': autocomplete.ModelSelect2Multiple(url='recipes:event-autocomplete'),
            'recipe_ingredients': autocomplete.ModelSelect2Multiple(url='ingredients:ingredient-autocomplete'),
            'recipe_file_storage': AddAnotherWidgetWrapper(autocomplete.ModelSelect2Multiple(url='images:file-autocomplete'), reverse_lazy('images:file_form'),),
        }