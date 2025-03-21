from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('ingredient/list', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredient/<pk>/update', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('ingredient/<pk>/delete', views.IngredientDelete.as_view(), name='ingredientdelete'),
    path('ingredient/<pk>/restock', views.IngredientRestock, name='ingredientrestock'),

    path('menuitem/list', views.MenuItemList.as_view(), name='menuitemlist'),
    path('menuitem/create', views.MenuItemCreate.as_view(), name='menuitemcreate'),
    path('menuitem/<pk>/update', views.MenuItemUpdate.as_view(), name='menuitemupdate'),
    path('menuitem/<pk>/delete', views.MenuItemDelete.as_view(), name='menuitemdelete'),

    path('reciperequirement/list', views.RecipeRequirementList.as_view(), name='reciperequirementlist'),
    path('reciperequirement/create', views.RecipeRequirementCreate.as_view(), name='reciperequirementcreate'),
    path('reciperequirement/<pk>/update', views.RecipeRequirementUpdate.as_view(), name='reciperequirementupdate'),
    path('reciperequirement/<pk>/delete', views.RecipeRequirementDelete.as_view(), name='reciperequirementdelete'),

    path('purchase/list', views.PurchaseList.as_view(), name='purchaselist'),
    path('purchase/create', views.PurchaseCreate.as_view(), name='purchasecreate'),
    path('purchase/<pk>/update', views.PurchaseUpdate.as_view(), name='purchaseupdate'),
    path('purchase/<pk>/delete', views.PurchaseDelete.as_view(), name='purchasedelete'),
]
