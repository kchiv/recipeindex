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
        self.fields['recipe_calories'].widget.attrs = {'class': 'form-select'}
        self.fields['recipe_protein'].widget.attrs = {'class': 'form-select'}
        self.fields['recipe_difficulty'].widget.attrs = {'class': 'form-select'}
        self.fields['recipe_time'].widget.attrs = {'class': 'form-select'}
        self.fields['recipe_priority'].widget.attrs = {'class': 'form-select'}

    class Meta:
        model = models.Recipe
        fields = '__all__'
        exclude = ['recipe_user']
        widgets = {
            'recipe_author': autocomplete.ModelSelect2Multiple(url='recipes:author-autocomplete'),
            'recipe_publisher': AddAnotherWidgetWrapper(autocomplete.ModelSelect2Multiple(url='recipes:publisher-autocomplete'), reverse_lazy('recipes:publisher_full_form'),),
            'recipe_cuisine': autocomplete.ModelSelect2Multiple(url='recipes:cuisine-autocomplete'),
            'recipe_meal': autocomplete.ModelSelect2Multiple(url='recipes:meal-autocomplete'),
            'recipe_dish': autocomplete.ModelSelect2Multiple(url='recipes:dish-autocomplete'),
            'recipe_category': autocomplete.ModelSelect2Multiple(url='recipes:category-autocomplete'),
            'recipe_event': autocomplete.ModelSelect2Multiple(url='recipes:event-autocomplete'),
            'recipe_ingredients': autocomplete.ModelSelect2Multiple(url='ingredients:ingredient-autocomplete'),
            'recipe_file_storage': AddAnotherWidgetWrapper(autocomplete.ModelSelect2Multiple(url='images:file-autocomplete'), reverse_lazy('images:file_form'),),
        }

class PublisherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['publisher_type'].widget.attrs = {'class': 'form-select'}

    class Meta:
        model = models.Publisher
        fields = '__all__'
        exclude = ['publisher_user']