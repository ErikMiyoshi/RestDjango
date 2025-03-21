from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import IngredientCreateForm, IngredientUpdateForm, IngredientRestockForm
from .forms import MenuItemCreateForm, MenuItemUpdateForm
from .forms import RecipeRequirementCreateForm, RecipeRequirementUpdateForm
from .forms import PurchaseCreateForm, PurchaseUpdateForm

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase


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

def IngredientRestock(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    current_quantity = ingredient.quantity

    if request.method == "POST":
        form = IngredientRestockForm(request.POST, instance=ingredient)
        
        if form.is_valid():
            restock_quantity = form.cleaned_data['quantity']

            ingredient.quantity = current_quantity + restock_quantity
            ingredient.save()

            return redirect("/ingredient/list")
    else:
        form = IngredientRestockForm()
        print(form.errors)

    context = { 'form': form, 
                'ingredient': ingredient,
    }

    return render(request, "inventory/ingredient_restock.html", context)

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


#Purchase Views
class PurchaseList(ListView):
    model = Purchase

class PurchaseCreate(CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    form_class = PurchaseCreateForm

class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    form_class = PurchaseUpdateForm

class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    success_url = "/purchase/list"

#Revnue, Cost, Profit
def Finance(request):
    cost = 0
    revenue = 0
    for purchase in Purchase.objects.all():
        revenue += purchase.menuitem.price

        for recipe in purchase.menuitem.reciperequirement_set.all():
            cost += recipe.ingredient.price * recipe.quantity
    profit = revenue - cost

    context = {
        "cost" : cost,
        "revenue": revenue,
        "profit": profit,
    }

    return render(request, "inventory/finance.html", context)

