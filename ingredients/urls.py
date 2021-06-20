from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'ingredients'

urlpatterns = [
    # path('recipe-submission/', views.recipe_url_form, name='recipe_url_form'),
    # path('form/', views.recipe_full_form, name='recipe_full_form'),
    url(r'^ingredient-autocomplete/$', views.IngredientAutocomplete.as_view(), name='ingredient-autocomplete'),
]