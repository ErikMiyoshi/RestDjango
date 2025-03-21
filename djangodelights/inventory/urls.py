from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('ingredient/list', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredient/<pk>/update', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('ingredient/<pk>/delete', views.IngredientDelete.as_view(), name='ingredientdelete'),

    path('menuitem/list', views.MenuItemList.as_view(), name='menuitemlist'),
    path('menuitem/create', views.MenuItemCreate.as_view(), name='menuitemcreate'),
    path('menuitem/<pk>/update', views.MenuItemUpdate.as_view(), name='menuitemupdate'),
    path('menuitem/<pk>/delete', views.MenuItemDelete.as_view(), name='menuitemdelete'),

]
