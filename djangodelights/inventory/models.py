from django.db import models

# Create your models here.
class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('Kg', 'Kilograms'),
        ('g', 'Grams'),
        ('L', 'Liters'),
        ('Un', 'Units'),
    ]    
    name = models.CharField(max_length = 30, null=False, blank=False)
    quantity = models.FloatField(null=False, blank=False, default=0)
    unit = models.CharField(max_length = 20, choices=UNIT_CHOICES, default="KG")
    price = models.FloatField(null=False, blank=False)  # price per unit

    def get_absolute_url(self):
        return '/ingredient/list'

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length = 30, null=False, blank=False)
    price = models.FloatField(null=False, blank=False, default=0)

    def get_absolute_url(self):
        return '/menuitem/list'

    def __str__(self):
        return self.name
    

class RecipeRequirement(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(null=False, blank=False, default=0)

    def get_absolute_url(self):
        return '/reciperequirement/list'
    
    def __str__(self):
        return self.menuitem.name
    
class Purchase(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return '/purchase/list'
    
    def __str__(self):
        return self.menuitem.name + " " + str(self.timestamp)