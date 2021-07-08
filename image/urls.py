from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'images'

urlpatterns = [
    # path('recipe-submission/', views.recipe_url_form, name='recipe_url_form'),
    # path('form/', views.recipe_full_form, name='recipe_full_form'),
    # path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    url(r'^file-autocomplete/$', views.FileAutocomplete.as_view(), name='file-autocomplete'),
]