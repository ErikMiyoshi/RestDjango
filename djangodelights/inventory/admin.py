from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement

# Correct model registrations
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)