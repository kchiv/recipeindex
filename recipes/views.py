from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .forms import RecipeForm

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
            return HttpResponseRedirect('/thanks/')
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