from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
    path('recipe-submission/', views.recipe_url_form, name='recipe_url_form'),
    path('form/', views.recipe_full_form, name='recipe_full_form'),
    path('form/edit/<int:recipe_id>/', views.recipe_full_form_edit, name='recipe_full_form_edit'),
    path('form/delete/<int:recipe_id>/', views.recipe_delete, name='recipe_delete'),
    path('publisher-form/', views.PublisherCreate.as_view(), name='publisher_full_form'),
    path('publisher-form/edit/<int:publisher_id>/', views.PublisherEdit.as_view(), name='publisher_full_form_edit'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('publisher/<int:publisher_id>/', views.publisher_detail, name='publisher_detail'),
    url(r'^author-autocomplete/$', views.AuthorAutocomplete.as_view(create_field='author_name'), name='author-autocomplete'),
    url(r'^publisher-autocomplete/$', views.PublisherAutocomplete.as_view(), name='publisher-autocomplete'),
    url(r'^cuisine-autocomplete/$', views.CuisineAutocomplete.as_view(create_field='cuisine_name'), name='cuisine-autocomplete'),
    url(r'^meal-autocomplete/$', views.MealAutocomplete.as_view(create_field='meal_name'), name='meal-autocomplete'),
    url(r'^dish-autocomplete/$', views.DishAutocomplete.as_view(create_field='dish_name'), name='dish-autocomplete'),
    url(r'^category-autocomplete/$', views.CategoryAutocomplete.as_view(create_field='category_name'), name='category-autocomplete'),
    url(r'^event-autocomplete/$', views.EventAutocomplete.as_view(create_field='event_name'), name='event-autocomplete'),
    url(r'^author-autocomplete-filter/$', views.AuthorAutocomplete.as_view(), name='author-autocomplete-filter'),
    url(r'^publisher-autocomplete-filter/$', views.PublisherAutocomplete.as_view(), name='publisher-autocomplete-filter'),
    url(r'^cuisine-autocomplete-filter/$', views.CuisineAutocomplete.as_view(), name='cuisine-autocomplete-filter'),
    url(r'^meal-autocomplete-filter/$', views.MealAutocomplete.as_view(), name='meal-autocomplete-filter'),
    url(r'^dish-autocomplete-filter/$', views.DishAutocomplete.as_view(), name='dish-autocomplete-filter'),
    url(r'^category-autocomplete-filter/$', views.CategoryAutocomplete.as_view(), name='category-autocomplete-filter'),
    url(r'^event-autocomplete-filter/$', views.EventAutocomplete.as_view(), name='event-autocomplete-filter'),
    url(r'^type-autocomplete-filter/$', views.TypeAutocomplete.as_view(), name='type-autocomplete-filter'),
]