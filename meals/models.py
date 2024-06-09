from django.db import models
from ingredients.models import Ingredient
# Create your models here.
class Meal(models.Model):
    main_objective_chocies = [
        ("Stare generală de bine", "Stare generală de bine"),
        ("Digestie îmbunătățită", "Digestie îmbunătățită"),
        ("Echilibru hormonal", "Echilibru hormonal"),
        ("Intolerante ", "Intolerante ")
    ]

    week_choices = [
        ('Luni', 'Luni'),
        ('Marti', 'Marti'),
        ('Miercuri', 'Miercuri'),
        ('Joi', 'Joi'),
        ('Vineri', 'Vineri'),
        ('Sambata', 'Sambata'),
        ('Duminica', 'Duminica')
    ]

    meal_type_choices = [
        ('Mic Dejun', 'Mic Dejun'),
        ('Pranz', 'Pranz'),
        ('Cina', 'Cina'),
        ('Gustare', 'Gustare')
    ]

    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=1000, default='No Description')
    # ingredient = models.TextField(max_length=1000)
    preparation = models.TextField(max_length=2000)
    nutritional_value = models.IntegerField(default=0)
    carbohydrates = models.IntegerField(default=0)
    proteins = models.IntegerField(default=0)
    fats = models.IntegerField(default=0)
    fibers = models.IntegerField(default=0)
    mealType = models.CharField(max_length=255, default='Mic Dejun', choices=meal_type_choices)
    preparationTime = models.IntegerField(default=0)
    lactoseFree = models.BooleanField(default=False)
    glutenFree = models.BooleanField(default=False)
    antiStress = models.BooleanField(default=False)
    energyLevelHigher = models.BooleanField(default=False)
    antiBloating = models.BooleanField(default=False)
    antiConstipation = models.BooleanField(default=False)
    improvementPCOS = models.BooleanField(default=False)
    improvementEndometriosis = models.BooleanField(default=False)
    dayOfTheWeek = models.CharField(max_length=100, default='Luni', choices=week_choices)
    image = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title