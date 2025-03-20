from django.db import models

# Create your models here.
class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('KG', 'Kilograma'),
    ]    
    name = models.CharField(max_length = 30, null=False, blank=False)
    quantity = models.FloatField()
    unit = models.CharField(max_length = 2, choices=UNIT_CHOICES, default="KG")
    price = models.FloatField()  # price per unit