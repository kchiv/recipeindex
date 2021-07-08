from django.shortcuts import render
from dal import autocomplete
from .models import ImageFile

# Create your views here.

class FileAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ImageFile.objects.all()

        if self.q:
            qs = qs.filter(image_file__icontains=self.q)
        
        return qs