from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import IngredientCreateForm, IngredientUpdateForm, IngredientRestockForm
from .forms import MenuItemCreateForm, MenuItemUpdateForm
from .forms import RecipeRequirementCreateForm, RecipeRequirementUpdateForm
from .forms import PurchaseCreateForm, PurchaseUpdateForm

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

from django.urls import reverse_lazy


def logout_view(request):
  logout(request)
  return redirect('home')

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"


# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

# Ingredient Views
class IngredientList(ListView):
    model = Ingredient

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientCreateForm

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    form_class = IngredientUpdateForm

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = "/ingredient/list"

@login_required
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

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemCreateForm

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update_form.html"
    form_class = MenuItemUpdateForm

class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete_form.html"
    success_url = "/menuitem/list"

# Recipe Requirement Views
class RecipeRequirementList(ListView):
    model = RecipeRequirement

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create_form.html"
    form_class = RecipeRequirementCreateForm

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_update_form.html"
    form_class = RecipeRequirementUpdateForm

class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_delete_form.html"
    success_url = "/reciperequirement/list"


#Purchase Views
class PurchaseList(ListView):
    model = Purchase

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    form_class = PurchaseCreateForm

class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    form_class = PurchaseUpdateForm

class PurchaseDelete(LoginRequiredMixin, DeleteView):
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

