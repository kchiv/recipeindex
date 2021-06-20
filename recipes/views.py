from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from dal import autocomplete
from .forms import RecipeForm
from .models import (
    Author,
    Publisher,
    Cuisine,
    Meal,
    Dish,
    Category,
    Event
)

# Create your views here.

def recipe_url_form(request):

    if request.method == 'POST':
        url_request = request.POST['url']
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
            form.save()
            return HttpResponseRedirect(reverse('recipes:recipe_url_form'))
    else:
        url = request.session.get('url_scrape')
        title = request.session.get('title_scrape')
        h1 = request.session.get('h1_scrape')
        data = {
            'recipe_url': url,
            'recipe_name_title_tag': title,
            'recipe_name_h1': h1
        }
        form = RecipeForm(initial=data)

    return render(request, 'recipes/recipe_full_form.html', {'form': form})

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