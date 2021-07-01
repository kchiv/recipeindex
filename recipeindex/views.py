from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from recipes.models import Recipe

class HomePageView(ListView):
    model = Recipe
    template_name = 'template_view/index.html'