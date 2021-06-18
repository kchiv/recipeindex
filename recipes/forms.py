from django.forms import ModelForm
from . import models

class RecipeForm(ModelForm):
    class Meta:
        model = models.Recipe
        fields = '__all__'