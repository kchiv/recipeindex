from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django_addanother.views import CreatePopupMixin
# from django.core.exceptions import DoesNotExist
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from dal import autocomplete
from .forms import (
    RecipeForm,
    PublisherForm
)
from .models import (
    Author,
    Publisher,
    Cuisine,
    Meal,
    Dish,
    Category,
    Event,
    Recipe,
    Type
)

# Create your views here.

#####################
# Recipe object views
#####################

def recipe_url_form(request):

    if request.method == 'POST':
        url_request = request.POST['url']

        try:
            url_lookup = Recipe.objects.get(recipe_url__exact=url_request)
            return render(request, 'recipes/recipe_url_form.html', {'error_message': 'URL already exists.'})
        except Recipe.DoesNotExist:
            pass

        request.session['url_scrape'] = url_request
        reqs = requests.get(url_request)

        soup = BeautifulSoup(reqs.text, 'html.parser')

        for title in soup.find_all('title'):
            # print(title.get_text())
            request.session['title_scrape'] = title.get_text()
        
        for h1 in soup.find_all('h1'):
            # print(h1.get_text())
            request.session['h1_scrape'] = h1.get_text()

        return redirect('recipes:recipe_full_form')


    return render(request, 'recipes/recipe_url_form.html')

def recipe_full_form(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse('recipes:recipe_detail', kwargs={'recipe_id': obj.id}))
    else:
        url = request.session.get('url_scrape')
        # Strip URL to root domain
        hostname = urlparse(url).hostname
        # Lookup publisher object using domain name
        publisher_lookup = Publisher.objects.filter(domain_name__icontains=hostname).first()
        title = request.session.get('title_scrape')

        # Publisher object conditional
        if publisher_lookup:
            # If publisher object exists, set variable to pk of object
            publisher_lookup = publisher_lookup.pk
        else:
            # If publisher object does not exist, return None
            publisher_lookup = None

        if 'youtube.com' in url:
            h1 = request.session.get('title_scrape')
        else:
            h1 = request.session.get('h1_scrape')
        data = {
            'recipe_url': url,
            'recipe_name_title_tag': title,
            'recipe_name_h1': h1,
            'recipe_publisher': publisher_lookup
        }
        form = RecipeForm(initial=data)

    return render(request, 'recipes/recipe_full_form.html', {'form': form})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


########################
# Publisher object views
########################

class PublisherCreate(CreatePopupMixin, CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'image/file_form.html'

    def get_success_url(self):
        return reverse('images:file_detail', kwargs={'file_id': self.object.pk})

def publisher_detail(request, publisher_id):
    publisher_obj = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, 'recipes/publisher_detail.html', {'publisher_obj': publisher_obj})

####################
# Autocomplete views
####################

class AuthorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Author.objects.all()

        if self.q:
            qs = qs.filter(author_name__icontains=self.q)
        
        return qs

class PublisherAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Publisher.objects.all()

        if self.q:
            qs = qs.filter(publisher_name__icontains=self.q)
        
        return qs

class CuisineAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Cuisine.objects.all()

        if self.q:
            qs = qs.filter(cuisine_name__icontains=self.q)
        
        return qs

class MealAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Meal.objects.all()

        if self.q:
            qs = qs.filter(meal_name__icontains=self.q)
        
        return qs

class DishAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Dish.objects.all()

        if self.q:
            qs = qs.filter(dish_name__icontains=self.q)
        
        return qs

class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(category_name__icontains=self.q)
        
        return qs

class EventAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Event.objects.all()

        if self.q:
            qs = qs.filter(event_name__icontains=self.q)
        
        return qs

class TypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Type.objects.all()

        if self.q:
            qs = qs.filter(type_name__icontains=self.q)
        
        return qs