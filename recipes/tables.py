from django.utils.html import format_html
from django_tables2 import tables, columns
from .models import Recipe

# class NameColumn(tables.Column):
#     def render(self, value):
#         return format_html('', value)

class RecipeTable(tables.Table):
    recipe_name_custom = columns.base.Column(verbose_name='Recipe Name')
    recipe_publisher = columns.base.Column(verbose_name='Publisher')
    recipe_created_date = columns.datetimecolumn.DateTimeColumn(format='SHORT_DATE_FORMAT', verbose_name='Created Date')

    def render_recipe_name_custom(self, value, record):
        return format_html('''
        <a href="{}" type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-html="true" title="<span><strong>Title:</strong> <em>{}</em></span><br><span><strong>H1:</strong> <em>{}</em></span>">
            {}
        </a>
        ''', record.get_absolute_url(), record.recipe_name_title_tag, record.recipe_name_h1, value)
    
    def render_recipe_publisher(self, value, record):
        print(value.__dict__)
        return format_html('<a href="?recipe_publisher={}">{}</a>', value.id, value)



    class Meta:
        model = Recipe
        template_name = 'django_tables2/bootstrap.html'
        fields = (
            'recipe_name_custom', 
            'recipe_publisher', 
            'recipe_rating', 
            'recipe_created_date', 
            'recipe_ingredients'
            )
