from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import IngredientCreateForm, IngredientUpdateForm
from .forms import MenuItemCreateForm, MenuItemUpdateForm
from .forms import RecipeRequirementCreateForm, RecipeRequirementUpdateForm

from .models import Ingredient, MenuItem, RecipeRequirement


# Create your views here.
def home(request):
    return render(request, "inventory/home.html")


# Ingredient Views
class IngredientList(ListView):
    model = Ingredient

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientCreateForm

class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    form_class = IngredientUpdateForm

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = "/ingredient/list"

# MenuItem Views
class MenuItemList(ListView):
    model = MenuItem

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemCreateForm

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update_form.html"
    form_class = MenuItemUpdateForm

class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete_form.html"
    success_url = "/menuitem/list"

# Recipe Requirement Views
class RecipeRequirementList(ListView):
    model = RecipeRequirement

class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create_form.html"
    form_class = RecipeRequirementCreateForm

class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_update_form.html"
    form_class = RecipeRequirementUpdateForm

class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_delete_form.html"
    success_url = "/reciperequirement/list"
