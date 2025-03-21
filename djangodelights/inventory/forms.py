from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement

#Ingredient Form
class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

#MenuItem Form
class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

#RecipeRequirement Form
class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class RecipeRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"