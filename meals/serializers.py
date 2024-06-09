from rest_framework import serializers
from .models import Meal
from ingredients.serializers import IngredientSerializer

class MealSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'preparation', 'nutritional_value', 'carbohydrates', 'proteins', 'fats', 'fibers', 'mealType', 'preparationTime', 'lactoseFree', 'glutenFree', 'antiStress', 'energyLevelHigher', 'antiBloating', 'antiConstipation', 'improvementPCOS', 'improvementEndometriosis', 'dayOfTheWeek', 'image', 'ingredient']