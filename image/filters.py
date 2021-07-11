from django.db.models import Q
from django import forms
from dal import autocomplete
import django_filters
from .models import ImageFile

class FileFilter(django_filters.FilterSet):
    image_name = django_filters.CharFilter(
        field_name='image_name',
        lookup_expr='icontains',
        label='Name', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    image_file = django_filters.CharFilter(
        field_name='image_file',
        lookup_expr='icontains',
        label='File Name', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    publication_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = ImageFile
        fields = [
            'image_name', 
            'image_file',
            'publication_date'
            ]
    
    def __init__(self, *args, **kwargs):
        super(FileFilter, self).__init__(*args, **kwargs)
        self.form.fields['publication_date'].widget.attrs = {'class': 'form-control date-between'}