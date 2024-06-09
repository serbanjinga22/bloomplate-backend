from django.db import models

# Create your models here.
class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('g', 'Grams'),
        ('kg', 'Kilograms'),
        ('ml', 'Milliliters'),
        ('l', 'Liters'),
        ('tsp', 'Teaspoons'),
        ('tbsp', 'Tablespoons'),
        ('cup', 'Cups'),
        ('piece', 'Pieces'),
    ]
    name = models.CharField(max_length=255, blank=False)
    unit_of_measure = models.CharField(max_length=255, blank=False, choices=UNIT_CHOICES, default='g')
    quantity = models.IntegerField(default=0)
    ingredientType = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name