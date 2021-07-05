from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from recipes.models import Recipe
from recipes.tables import RecipeTable
from recipes.filters import RecipeFilter
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Recipe
    table_class = RecipeTable
    template_name = 'template_view/index.html'
    filterset_class = RecipeFilter
    login_url = '/admin/'
    redirect_field_name = 'home'