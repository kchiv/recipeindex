from django.utils.html import format_html
from django_tables2 import tables, columns
from .models import Recipe

# class NameColumn(tables.Column):
#     def render(self, value):
#         return format_html('', value)

class RecipeTable(tables.Table):
    recipe_name_custom = columns.base.Column(verbose_name='Recipe Name')
    recipe_publisher = columns.base.Column(verbose_name='Publisher')
    recipe_rating = columns.base.Column(verbose_name='Rating')
    recipe_full_ingredients = columns.base.Column(verbose_name='Ingredients')
    recipe_full_steps = columns.base.Column(verbose_name='Steps')
    recipe_alterations = columns.base.Column(verbose_name='Alterations')
    recipe_notes = columns.base.Column(verbose_name='Notes')
    recipe_created_date = columns.datetimecolumn.DateTimeColumn(format='SHORT_DATE_FORMAT', verbose_name='Created Date')

    def render_recipe_name_custom(self, value, record):
        return format_html('''
        <a href="{}" type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-html="true" title="<span><strong>Title:</strong> <em>{}</em></span><br><span><strong>H1:</strong> <em>{}</em></span>">
            {}
        </a>
        ''', record.get_absolute_url(), record.recipe_name_title_tag, record.recipe_name_h1, value)
    
    def render_recipe_publisher(self, value, record):
        return format_html('<a href="?recipe_publisher={}">{}</a>', value.id, value)

    def render_recipe_rating(self, value, record):
        if value <= 5:
            return format_html('<span class="badge bg-danger">{}</span>', value)
        elif value < 8:
            return format_html('<span class="badge bg-warning text-dark">{}</span>', value)
        else:
            return format_html('<span class="badge bg-success">{}</span>', value)

    def render_recipe_full_ingredients(self, value, record):
        if value:
            return format_html('<a href="{}#item-d-ingredients"><span style="color: green;"><i class="fas fa-check-circle"></i></span></a>', record.get_absolute_url())
    
    def render_recipe_full_steps(self, value, record):
        if value:
            return format_html('<a href="{}#item-d-instructions"><span style="color: green;"><i class="fas fa-check-circle"></i></span></a>', record.get_absolute_url())
    
    def render_recipe_alterations(self, value, record):
        if value:
            return format_html('<a href="{}#item-d-alterations"><span style="color: green;"><i class="fas fa-check-circle"></i></span></a>', record.get_absolute_url())
    
    def render_recipe_notes(self, value, record):
        if value:
            return format_html('<a href="{}#item-d-notes"><span style="color: green;"><i class="fas fa-check-circle"></i></span></a>', record.get_absolute_url())
    
    def render_recipe_instantpot(self, value, record):
        if value == True:
            return format_html('<a href="{}#item-instantpot"><span style="color: green;"><i class="fas fa-check-circle"></i></span></a>', record.get_absolute_url())
        else:
            return format_html('<a href="{}#item-instantpot"><span style="color: red;"><i class="fas fa-times-circle"></i></span></a>', record.get_absolute_url())


    class Meta:
        model = Recipe
        template_name = 'django_tables2/bootstrap.html'
        fields = (
            'recipe_name_custom', 
            'recipe_publisher', 
            'recipe_rating',
            'recipe_full_ingredients',
            'recipe_full_steps',
            'recipe_alterations',
            'recipe_notes',
            'recipe_instantpot',
            'recipe_created_date', 
            'recipe_ingredients'
            )
