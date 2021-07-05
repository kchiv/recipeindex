from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from recipes.models import Recipe
from recipes.tables import RecipeTable
from recipes.filters import RecipeFilter
from django_tables2.views import SingleTableMixin

class HomePageView(SingleTableMixin, FilterView):
    model = Recipe
    table_class = RecipeTable
    template_name = 'template_view/index.html'
    filterset_class = RecipeFilter