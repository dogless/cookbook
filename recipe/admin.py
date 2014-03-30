from django.contrib import admin
from recipe.models import Recipe, Step, Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
