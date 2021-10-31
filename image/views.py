from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_addanother.views import CreatePopupMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from dal import autocomplete
from .models import ImageFile
from .forms import FileForm

# Create your views here.

class FileCreate(LoginRequiredMixin, CreatePopupMixin, CreateView):
    model = ImageFile
    form_class = FileForm
    template_name = 'image/file_form.html'

    def get_success_url(self):
        return reverse('images:file_detail', kwargs={'file_id': self.object.pk})
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.image_user = self.request.user
        self.object.save()
        return super().form_valid(form)

class FileEdit(LoginRequiredMixin, UpdateView):
    model = ImageFile
    form_class = FileForm
    template_name = 'image/file_form.html'

    def get_object(self):
        return ImageFile.objects.get(pk=self.kwargs['file_id'], image_user=self.request.user)

    def get_success_url(self):
        return reverse('file_table')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context

class FileDelete(LoginRequiredMixin, DeleteView):
    model = ImageFile

    def get_object(self):
        return ImageFile.objects.get(pk=self.kwargs['file_id'], image_user=self.request.user)

    def get_success_url(self):
        return reverse('file_table')

@login_required()
def file_detail(request, file_id):
    file_obj = get_object_or_404(ImageFile, pk=file_id, image_user=request.user)
    return render(request, 'image/file_detail.html', {'file_obj': file_obj, 'file_detail': True})

####################
# Autocomplete views
####################

class FileAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ImageFile.objects.filter(image_user=self.request.user)

        if self.q:
            qs = qs.filter(image_file__icontains=self.q)
        
        return qs