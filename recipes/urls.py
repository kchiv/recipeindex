from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('recipe-submission/', views.recipe_url_form, name='recipe_url_form'),
    path('form/', views.recipe_full_form, name='recipe_full_form'),
]