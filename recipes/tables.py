from django.utils.html import format_html
from django_tables2 import tables, columns
from .models import Recipe, Publisher

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

def object_list_sizing(value, field_name):
        full_html_str = ''
        if value:
            if value.size_order == 1:
                full_html_str = '<a href="?{}={}"><span class="badge bg-success">Low</span></a>'.format(field_name, value.id)
            elif value.size_order == 2:
                full_html_str = '<a href="?{}={}"><span class="badge bg-warning text-dark">Medium</span></a>'.format(field_name, value.id)
            elif value.size_order == 3:
                full_html_str = '<a href="?{}={}"><span class="badge bg-danger">High</span></a>'.format(field_name, value.id)
            elif value.size_order == 4:
                full_html_str = '<a href="?{}={}"><span class="badge bg-purple">Very High</span></a>'.format(field_name, value.id)
        else:
            full_html_str = '—'
        return format_html(full_html_str)

class RecipeTable(tables.Table):
    recipe_name_custom = columns.base.Column(verbose_name='Recipe Name')
    recipe_url = columns.base.Column(verbose_name='URL')
    recipe_publisher = columns.base.Column(verbose_name='Publisher', orderable=False)
    recipe_author = columns.base.Column(verbose_name='Author', orderable=False)
    recipe_type = columns.base.Column(verbose_name='Type', accessor='recipe_publisher', orderable=False)
    recipe_rating = columns.base.Column(verbose_name='Rating')
    recipe_full_ingredients = columns.base.Column(verbose_name='Ingredients')
    recipe_full_steps = columns.base.Column(verbose_name='Steps')
    recipe_alterations = columns.base.Column(verbose_name='Alterations')
    recipe_notes = columns.base.Column(verbose_name='Notes')
    recipe_instantpot = columns.base.Column(verbose_name='Instantpot')
    recipe_cuisine = columns.base.Column(verbose_name='Cuisine', orderable=False)
    recipe_meal = columns.base.Column(verbose_name='Meal', orderable=False)
    recipe_dish = columns.base.Column(verbose_name='Dish', orderable=False)
    recipe_category = columns.base.Column(verbose_name='Category', orderable=False)
    recipe_ingredients = columns.base.Column(verbose_name='Ingredients', orderable=False, attrs={'th': {'style': 'width: 10%'}})
    recipe_event = columns.base.Column(verbose_name='Event', orderable=False)
    recipe_calories = columns.base.Column(verbose_name='Calories')
    recipe_protein = columns.base.Column(verbose_name='Protein')
    recipe_difficulty = columns.base.Column(verbose_name='Difficulty')
    recipe_time = columns.base.Column(verbose_name='Time')
    recipe_time_amount = columns.base.Column(verbose_name='Time (Hours)')
    recipe_priority = columns.base.Column(verbose_name='Priority')
    recipe_wayback_url = columns.base.Column(verbose_name='Wayback URL')
    recipe_created_date = columns.datetimecolumn.DateTimeColumn(format='SHORT_DATE_FORMAT', verbose_name='Date')

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
    
    def render_recipe_publisher(self, value):
        return object_list_rend(value, 'recipe_publisher')

    def render_recipe_author(self, value):
        return object_list_rend(value, 'recipe_author')
    
    def render_recipe_type(self, value, record):
        full_html_str = ''
        # for i in value.all():
        #     print(i.publisher_type)
        if value.all():
            for obj in value.all():
                obj_str = '<a href="?{}={}">{}</a>, '.format('recipe_type', obj.publisher_type.id, obj.publisher_type.type_name)
                full_html_str += obj_str
            full_html_str = full_html_str[:-2]
        else:
            full_html_str = '—'
        return format_html(full_html_str)

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
    
    def render_recipe_event(self, value):
        return object_list_rend(value, 'recipe_event')
    
    def render_recipe_calories(self, value):
        return object_list_sizing(value, 'recipe_calories')
    
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
    
    def render_recipe_difficulty(self, value):
        return object_list_sizing(value, 'recipe_difficulty')
    
    def render_recipe_time(self, value):
        return object_list_sizing(value, 'recipe_time')
    
    def render_recipe_priority(self, value):
        return object_list_sizing(value, 'recipe_priority')
    
    def render_recipe_wayback_url(self, value):
        return format_html('''
        <a target="_blank" href="{}" type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-html="true" title="<span><em>{}</em></span>">
            <i class="fas fa-external-link-alt"></i>
        </a>
        ''', value, value)

    class Meta:
        model = Recipe
        order_by = '-recipe_rating'
        attrs = {"style": "width: 300%;"}
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'recipe_name_custom',
            'recipe_url',
            'recipe_publisher', 
            'recipe_author',
            'recipe_type',
            'recipe_rating',
            'recipe_full_ingredients',
            'recipe_full_steps',
            'recipe_alterations',
            'recipe_notes',
            'recipe_instantpot',
            'recipe_cuisine',
            'recipe_meal',
            'recipe_dish',
            'recipe_category',
            'recipe_ingredients',
            'recipe_event',
            'recipe_calories',
            'recipe_protein',
            'recipe_difficulty',
            'recipe_time',
            'recipe_time_amount',
            'recipe_priority',
            'recipe_wayback_url',
            'recipe_created_date'
            )
