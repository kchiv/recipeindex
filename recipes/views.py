from django.shortcuts import render

# Create your views here.

def recipe_submission(request):
    return render(request, 'recipes/recipe_submission.html')