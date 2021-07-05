from django.utils.html import format_html
from django_tables2 import tables, columns
from .models import Recipe

# class NameColumn(tables.Column):
#     def render(self, value):
#         return format_html('', value)

def object_list_rend(value, field_name):
        full_html_str = ''
        if value.all():
            for obj in value.all():
                obj_str = '<a href="?{}={}">{}</a>, '.format(field_name, obj.id, obj)
                full_html_str += obj_str
            full_html_str = full_html_str[:-2]
        else:
            full_html_str = '—'
        return format_html(full_html_str)

class RecipeTable(tables.Table):
    recipe_name_custom = columns.base.Column(verbose_name='Recipe Name')
    recipe_url = columns.base.Column(verbose_name='URL')
    recipe_publisher = columns.base.Column(verbose_name='Publisher')
    recipe_author = columns.base.Column(verbose_name='Author')
    recipe_rating = columns.base.Column(verbose_name='Rating')
    recipe_full_ingredients = columns.base.Column(verbose_name='Ingredients')
    recipe_full_steps = columns.base.Column(verbose_name='Steps')
    recipe_alterations = columns.base.Column(verbose_name='Alterations')
    recipe_notes = columns.base.Column(verbose_name='Notes')
    recipe_instantpot = columns.base.Column(verbose_name='Instantpot')
    recipe_created_date = columns.datetimecolumn.DateTimeColumn(format='SHORT_DATE_FORMAT', verbose_name='Created Date')
    recipe_cuisine = columns.base.Column(verbose_name='Cuisine')
    recipe_meal = columns.base.Column(verbose_name='Meal')
    recipe_dish = columns.base.Column(verbose_name='Dish')
    recipe_category = columns.base.Column(verbose_name='Category')
    recipe_ingredients = columns.base.Column(verbose_name='Ingredients')
    recipe_calories = columns.base.Column(verbose_name='Calories')
    recipe_protein = columns.base.Column(verbose_name='Protein')

    def render_recipe_name_custom(self, value, record):
        return format_html('''
        <a href="{}" type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-html="true" title="<span><strong>Title:</strong> <em>{}</em></span><br><span><strong>H1:</strong> <em>{}</em></span>">
            {}
        </a>
        ''', record.get_absolute_url(), record.recipe_name_title_tag, record.recipe_name_h1, value)
    
    def render_recipe_url(self, value):
        return format_html('''
        <a href="{}" type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-html="true" title="<span><em>{}</em></span>">
            <i class="fas fa-external-link-alt"></i>
        </a>
        ''', value, value)
    
    def render_recipe_publisher(self, value, record):
        return format_html('<a href="?recipe_publisher={}">{}</a>', value.id, value)

    def render_recipe_author(self, value):
        return object_list_rend(value, 'recipe_author')

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
    
    def render_recipe_cuisine(self, value):
        return object_list_rend(value, 'recipe_cuisine')
    
    def render_recipe_meal(self, value):
        return object_list_rend(value, 'recipe_meal')
    
    def render_recipe_dish(self, value):
        return object_list_rend(value, 'recipe_dish')
    
    def render_recipe_category(self, value):
        return object_list_rend(value, 'recipe_category')
    
    def render_recipe_ingredients(self, value):
        return object_list_rend(value, 'recipe_ingredients')
    
    def render_recipe_calories(self, value):
        full_html_str = ''
        if value:
            if value.size_order == 1:
                full_html_str = '<a href="?recipe_calories={}"><span class="badge bg-success">Low</span></a>'.format(value.id)
            elif value.size_order == 2:
                full_html_str = '<a href="?recipe_calories={}"><span class="badge bg-warning text-dark">Medium</span></a>'.format(value.id)
            elif value.size_order == 3:
                full_html_str = '<a href="?recipe_calories={}"><span class="badge bg-danger">High</span></a>'.format(value.id)
            elif value.size_order == 4:
                full_html_str = '<a href="?recipe_calories={}"><span class="badge bg-purple">Very High</span></a>'.format(value.id)
        else:
            full_html_str = '—'
        return format_html(full_html_str)
    
    def render_recipe_protein(self, value):
        full_html_str = ''
        if value:
            if value.size_order == 1:
                full_html_str = '<a href="?recipe_protein={}"><span class="badge bg-danger">Low</span></a>'.format(value.id)
            elif value.size_order == 2:
                full_html_str = '<a href="?recipe_protein={}"><span class="badge bg-warning text-dark">Medium</span></a>'.format(value.id)
            elif value.size_order == 3:
                full_html_str = '<a href="?recipe_protein={}"><span class="badge bg-success">High</span></a>'.format(value.id)
            elif value.size_order == 4:
                full_html_str = '<a href="?recipe_protein={}"><span class="badge bg-success">Very High</span></a>'.format(value.id)
        else:
            full_html_str = '—'
        return format_html(full_html_str)

    class Meta:
        model = Recipe
        template_name = 'django_tables2/bootstrap.html'
        fields = (
            'recipe_name_custom',
            'recipe_url',
            'recipe_publisher', 
            'recipe_author',
            'recipe_rating',
            'recipe_full_ingredients',
            'recipe_full_steps',
            'recipe_alterations',
            'recipe_notes',
            'recipe_instantpot',
            'recipe_created_date', 
            'recipe_cuisine',
            'recipe_meal',
            'recipe_dish',
            'recipe_category',
            'recipe_ingredients',
            'recipe_calories',
            'recipe_protein'
            )
