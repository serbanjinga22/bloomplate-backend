from django.db import models

# Create your models here.
class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('g', 'Grame'),
        ('kg', 'Kilograme'),
        ('ml', 'Mililitri'),
        ('l', 'Litri'),
        ('tsp', 'Lingurițe'),
        ('tbsp', 'Linguri'),
        ('cup', 'Căni'),
        ('piece', 'Bucăți'),
    ]

    INGREDIENT_TYPE_CHOICES = [
        ('Lactate, brânză și ouă', 'Lactate, brânză și ouă'),
        ('Legume și fructe', 'Legume și fructe'),
        ('Carne și pește', 'Carne și pește'),
        ('Cereale, făinoase, nuci', 'Cereale, făinoase, nuci'),
        ('Condimente și Uleiuri', 'Condimente și Uleiuri'),
        ('Diverse', 'Diverse'),
    ]
    name = models.CharField(max_length=255, blank=False)
    unit_of_measure = models.CharField(max_length=255, blank=False, choices=UNIT_CHOICES, default='g')
    quantity = models.IntegerField(default=0)
    ingredientType = models.CharField(max_length=255, blank=True, choices=INGREDIENT_TYPE_CHOICES, default='Diverse')

    def __str__(self):
        return self.name