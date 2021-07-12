from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
            url_lookup = Recipe.objects.get(recipe_url__exact=url_request, recipe_user=request.user)
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
        
        # scrape publisher ingredients + steps
        hostname = urlparse(url_request).hostname
        publisher_lookup = Publisher.objects.filter(domain_name__icontains=hostname, publisher_user=request.user).first()
        if publisher_lookup:
            print(publisher_lookup.ingredients_xpath)
            tester = soup.find_all('div', {'class': 'ingredients'})
            html_str = ''
            for t in tester:
                html_str += str(t)
            print(html_str)
            request.session['ingredient_scrape'] = str(html_str)

        return redirect('recipes:recipe_full_form')


    return render(request, 'recipes/recipe_url_form.html')

def recipe_full_form(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        recipe_url_value = request.POST.get('recipe_url')
        recipe_url_lookup = Recipe.objects.filter(recipe_url=recipe_url_value, recipe_user=request.user)

        if recipe_url_lookup:
            return render(request, 'recipes/recipe_full_form.html', {'form': form, 'custom_error': 'The submited URL already exists.'})
        else:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.recipe_user = request.user
                obj.save()
                return HttpResponseRedirect(reverse('recipes:recipe_detail', kwargs={'recipe_id': obj.id}))
    else:
        url = request.session.get('url_scrape')
        ingredient_list = request.session.get('ingredient_scrape')
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
            'recipe_publisher': publisher_lookup,
            'recipe_full_ingredients': ingredient_list
        }
        form = RecipeForm(initial=data)

    return render(request, 'recipes/recipe_full_form.html', {'form': form})

def recipe_full_form_edit(request, recipe_id):
    instance = Recipe.objects.get(pk=recipe_id, recipe_user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=instance)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse('recipes:recipe_detail', kwargs={'recipe_id': obj.id}))
    else:
        form = RecipeForm(instance=instance)

    return render(request, 'recipes/recipe_full_form.html', {'form': form, 'edit': True, 'instance': instance})

def recipe_delete(request, recipe_id):
    instance = Recipe.objects.get(pk=recipe_id, recipe_user=request.user)
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect(reverse('home'))
    else:
        form = RecipeForm(instance=instance)

    return render(request, 'recipes/recipe_full_form.html', {'form': form, 'edit': True, 'instance': instance})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, recipe_user=request.user)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'recipe_detail': True})


########################
# Publisher object views
########################

class PublisherCreate(CreatePopupMixin, CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'recipes/publisher_form.html'

    def get_success_url(self):
        return reverse('publisher_table')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.publisher_user = self.request.user
        self.object.save()
        return super().form_valid(form)

class PublisherEdit(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'recipes/publisher_form.html'

    def get_object(self):
        return Publisher.objects.get(pk=self.kwargs['publisher_id'], publisher_user=self.request.user)

    def get_success_url(self):
        return reverse('publisher_table')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context

class PublisherDelete(DeleteView):
    model = Publisher

    def get_object(self):
        return Publisher.objects.get(pk=self.kwargs['publisher_id'], publisher_user=self.request.user)

    def get_success_url(self):
        return reverse('publisher_table')

def publisher_detail(request, publisher_id):
    publisher_obj = get_object_or_404(Publisher, pk=publisher_id, publisher_user=request.user)
    return render(request, 'recipes/publisher_detail.html', {'publisher_obj': publisher_obj, 'publisher_detail': True})

####################
# Autocomplete views
####################

class AuthorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Author.objects.filter(author_user=self.request.user)

        if self.q:
            qs = qs.filter(author_name__icontains=self.q)
        
        return qs
    
    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'author_user': self.request.user})

class PublisherAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Publisher.objects.filter(publisher_user=self.request.user)

        if self.q:
            qs = qs.filter(publisher_name__icontains=self.q)
        
        return qs
    
    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'publisher_user': self.request.user})

class CuisineAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Cuisine.objects.filter(cuisine_user=self.request.user)

        if self.q:
            qs = qs.filter(cuisine_name__icontains=self.q)
        
        return qs
    
    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'cuisine_user': self.request.user})

class MealAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Meal.objects.filter(meal_user=self.request.user)

        if self.q:
            qs = qs.filter(meal_name__icontains=self.q)
        
        return qs
    
    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'meal_user': self.request.user})

class DishAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Dish.objects.filter(dish_user=self.request.user)

        if self.q:
            qs = qs.filter(dish_name__icontains=self.q)
        
        return qs
    
    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'dish_user': self.request.user})

class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.filter(category_user=self.request.user)

        if self.q:
            qs = qs.filter(category_name__icontains=self.q)
        
        return qs
    
    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'category_user': self.request.user})

class EventAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Event.objects.filter(event_user=self.request.user)

        if self.q:
            qs = qs.filter(event_name__icontains=self.q)
        
        return qs

    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'event_user': self.request.user})

class TypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Type.objects.all()

        if self.q:
            qs = qs.filter(type_name__icontains=self.q)
        
        return qs