from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django_addanother.views import CreatePopupMixin
from dal import autocomplete
from .models import ImageFile
from .forms import FileForm

# Create your views here.

class FileCreate(CreatePopupMixin, CreateView):
    model = ImageFile
    form_class = FileForm
    template_name = 'image/file_form.html'

    def get_success_url(self):
        return reverse('images:file_detail', kwargs={'file_id': self.object.pk})

def file_detail(request, file_id):
    file_obj = get_object_or_404(ImageFile, pk=file_id)
    return render(request, 'image/file_detail.html', {'file_obj': file_obj})

class FileAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ImageFile.objects.all()

        if self.q:
            qs = qs.filter(image_file__icontains=self.q)
        
        return qs