from django.utils.html import format_html
from django_tables2 import tables, columns
from django_tables2.utils import A
from .models import ImageFile

class FileTable(tables.Table):
    image_name = columns.base.Column(verbose_name='Name')
    id = columns.base.Column(verbose_name='Detail')
    file_edit = columns.TemplateColumn(
        '<a class="btn btn-secondary" href="{% url \'images:file_form_edit\' record.id %}"><i class="fas fa-edit"></i></a>', 
        verbose_name='Edit', 
        orderable=False)
    image_file = columns.base.Column(verbose_name='File Name')
    publication_date = columns.datetimecolumn.DateTimeColumn(format='SHORT_DATE_FORMAT', verbose_name='Date')

    def render_id(self, value, record):
        return format_html(
            '<a href="{}" class="btn btn-primary" type="button"><i class="fas fa-link"></i></a>',
            record.get_absolute_url())

    def render_image_name(self, value, record):
        return format_html(
            '<a href="{}" type="button" class="btn btn-secondary">{}</a>',
            record.get_absolute_url(), 
            record.image_name)

    def render_image_file(self, value):
        return format_html('<a target="_blank" href="{}">{}</a>', value.url, value)

    class Meta:
        model = ImageFile
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'image_name',
            'id',
            'file_edit',
            'image_file',
            'publication_date',
        )