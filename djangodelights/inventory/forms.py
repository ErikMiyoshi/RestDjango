from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

#Ingredient Form
class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class IngredientRestockForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["quantity"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].initial = {'quantity': None}

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
    
#Purchase Form
class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

class PurchaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"