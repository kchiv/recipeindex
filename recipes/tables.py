from django.utils.html import format_html
from django_tables2 import tables, columns
from .models import Recipe

# class NameColumn(tables.Column):
#     def render(self, value):
#         return format_html('', value)

class RecipeTable(tables.Table):
    recipe_name_custom = columns.base.Column(verbose_name='Recipe Name')
    recipe_created_date = columns.datetimecolumn.DateTimeColumn(format='SHORT_DATE_FORMAT')

    def render_recipe_name_custom(self, value, record):
        return format_html('''
        <a href="{}" type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-html="true" title="<p>{}</p><p>{}</p>">
            {}
        </a>
        ''', record.get_absolute_url(), record.recipe_name_title_tag, record.recipe_name_h1, value)



    class Meta:
        model = Recipe
        template_name = 'django_tables2/bootstrap.html'
        fields = ('recipe_name_custom', 'recipe_rating', 'recipe_created_date', 'recipe_ingredients')
