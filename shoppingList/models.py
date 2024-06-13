from django.db import models

# Create your models here.
class ShoppingList(models.Model):
    shoppingList = models.TextField(max_length=2000, blank=True, default='')
    lactoseFree = models.BooleanField(default=False)
    glutenFree = models.BooleanField(default=False)
    antiStress = models.BooleanField(default=False)
    energyLevelHigher = models.BooleanField(default=False)
    antiBloating = models.BooleanField(default=False)
    antiConstipation = models.BooleanField(default=False)
    improvementPCOS = models.BooleanField(default=False)
    improvementEndometriosis = models.BooleanField(default=False)