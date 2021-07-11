from django.utils.html import format_html
from django_tables2 import tables, columns
from django_tables2.utils import A
from .models import ImageFile

class FileTable(tables.Table):

    class Meta:
        model = ImageFile
        template_name = 'django_tables2/bootstrap-responsive.html'