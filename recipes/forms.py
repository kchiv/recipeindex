from django import forms
from dal import autocomplete
from . import models

class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = models.Recipe
        fields = '__all__'
        widgets = {
            'recipe_author': autocomplete.ModelSelect2Multiple(url='recipes:author-autocomplete')
        }