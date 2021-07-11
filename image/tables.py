from django.utils.html import format_html
from django_tables2 import tables, columns
from django_tables2.utils import A
from .models import ImageFile

class FileTable(tables.Table):
    file_edit = columns.TemplateColumn(
        '<a class="btn btn-secondary" href="{% url \'images:file_form_edit\' record.id %}"><i class="fas fa-edit"></i></a>', 
        verbose_name='Edit', 
        orderable=False)

    class Meta:
        model = ImageFile
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'id',
            'image_name',
            'file_edit',
            'image_file',
            'publication_date',
        )