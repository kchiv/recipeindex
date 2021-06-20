from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
    path('recipe-submission/', views.recipe_url_form, name='recipe_url_form'),
    path('form/', views.recipe_full_form, name='recipe_full_form'),
    url(r'^author-autocomplete/$', views.AuthorAutocomplete.as_view(), name='author-autocomplete'),
    url(r'^publisher-autocomplete/$', views.PublisherAutocomplete.as_view(), name='publisher-autocomplete'),
    url(r'^cuisine-autocomplete/$', views.CuisineAutocomplete.as_view(), name='cuisine-autocomplete'),
    url(r'^meal-autocomplete/$', views.MealAutocomplete.as_view(), name='meal-autocomplete'),
    url(r'^dish-autocomplete/$', views.DishAutocomplete.as_view(), name='dish-autocomplete'),
    url(r'^category-autocomplete/$', views.CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^event-autocomplete/$', views.EventAutocomplete.as_view(), name='event-autocomplete'),
]