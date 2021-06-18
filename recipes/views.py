from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

# Create your views here.

def recipe_submission(request):

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

        return redirect('recipes:recipe_form')


    return render(request, 'recipes/recipe_submission.html')

def recipe_form(request):
    url = request.session.get('url_scrape')
    title = request.session.get('title_scrape')
    h1 = request.session.get('h1_scrape')

    print(url, title, h1)
    return render(request, 'recipes/recipe_submission.html')