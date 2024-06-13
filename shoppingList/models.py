from django.db import models

# Create your models here.
class ShoppingList(models.Model):
    shoppingList = models.CharField(max_length=2000, blank=True, default='')
