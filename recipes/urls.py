from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('recipe-submission/', views.recipe_submission, name='recipe_submission'),
    path('form/', views.recipe_form, name='recipe_form'),
]