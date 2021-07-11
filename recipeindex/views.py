from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from recipes.models import Recipe, Publisher
from image.models import ImageFile
from recipes.tables import RecipeTable, PublisherTable
from image.tables import FileTable
from recipes.filters import RecipeFilter
from image.filters import FileFilter
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class RecipeView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Recipe
    table_class = RecipeTable
    template_name = 'template_view/index.html'
    filterset_class = RecipeFilter
    login_url = '/admin/'
    redirect_field_name = 'home'

class PublisherView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Publisher
    table_class = PublisherTable
    template_name = 'template_view/index.html'
    # filterset_class = RecipeFilter
    login_url = '/admin/'
    redirect_field_name = 'home'

class FileView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = ImageFile
    table_class = FileTable
    template_name = 'template_view/index.html'
    filterset_class = FileFilter
    login_url = '/admin/'
    redirect_field_name = 'home'
