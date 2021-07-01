from django_tables2 import tables, columns
from .models import Recipe

class RecipeTable(tables.Table):
    # date = columns.base.Column()
    date = columns.datetimecolumn.DateTimeColumn(format='SHORT_DATE_FORMAT', short=True)


    def render_date(self, record):
        return record.recipe_created_date

    class Meta:
        model = Recipe
        template_name = 'django_tables2/bootstrap.html'
        fields = ('recipe_name_custom', 'recipe_rating', 'recipe_created_date')
