from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
    path('recipe-submission/', views.recipe_url_form, name='recipe_url_form'),
    path('form/', views.recipe_full_form, name='recipe_full_form'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    url(r'^author-autocomplete/$', views.AuthorAutocomplete.as_view(create_field='author_name'), name='author-autocomplete'),
    url(r'^publisher-autocomplete/$', views.PublisherAutocomplete.as_view(create_field='publisher_name'), name='publisher-autocomplete'),
    url(r'^cuisine-autocomplete/$', views.CuisineAutocomplete.as_view(create_field='cuisine_name'), name='cuisine-autocomplete'),
    url(r'^meal-autocomplete/$', views.MealAutocomplete.as_view(create_field='meal_name'), name='meal-autocomplete'),
    url(r'^dish-autocomplete/$', views.DishAutocomplete.as_view(create_field='dish_name'), name='dish-autocomplete'),
    url(r'^category-autocomplete/$', views.CategoryAutocomplete.as_view(create_field='category_name'), name='category-autocomplete'),
    url(r'^event-autocomplete/$', views.EventAutocomplete.as_view(create_field='event_name'), name='event-autocomplete'),
]