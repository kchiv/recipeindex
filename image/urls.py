from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'images'

urlpatterns = [
    # path('recipe-submission/', views.recipe_url_form, name='recipe_url_form'),
    path('form/', views.FileCreate.as_view(), name='file_form'),
    path('form/edit/<int:file_id>/', views.FileEdit.as_view(), name='file_form_edit'),
    path('form/delete/<int:file_id>/', views.FileDelete.as_view(), name='file_delete'),
    path('<int:file_id>/', views.file_detail, name='file_detail'),
    url(r'^file-autocomplete/$', views.FileAutocomplete.as_view(), name='file-autocomplete'),
]