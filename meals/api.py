from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Meal
from .serializers import MealSerializer
from django.contrib.auth import get_user_model
from collections import defaultdict

User = get_user_model()

class MealList(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealDetail(generics.RetrieveAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

from django.utils import timezone

class MealMatchUser(generics.ListAPIView):
    serializer_class = MealSerializer

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['user_id'])
        weeks_since_creation = max(1, (timezone.now() - user.date_joined).days // 7)
        return Meal.objects.filter(
            lactoseFree=user.lactoseFree,
            glutenFree=user.glutenFree,
            antiStress=user.antiStress,
            energyLevelHigher=user.energyLevelHigher,
            antiBloating=user.antiBloating,
            antiConstipation=user.antiConstipation,
            improvementPCOS=user.improvementPCOS,
            improvementEndometriosis=user.improvementEndometriosis,
            weekNumber=weeks_since_creation
        )
    
class IngredientTotals(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=self.kwargs['user_id'])
        meals = Meal.objects.filter(
            lactoseFree=user.lactoseFree,
            glutenFree=user.glutenFree,
            antiStress=user.antiStress,
            energyLevelHigher=user.energyLevelHigher,
            antiBloating=user.antiBloating,
            antiConstipation=user.antiConstipation,
            improvementPCOS=user.improvementPCOS,
            improvementEndometriosis=user.improvementEndometriosis
        )

        ingredient_totals = defaultdict(lambda: defaultdict(lambda: {'quantity': 0, 'unit_of_measure': ''}))
        for meal in meals:
            for ingredient in meal.ingredient.all():
                ingredient_totals[ingredient.ingredientType][ingredient.name]['quantity'] += ingredient.quantity
                ingredient_totals[ingredient.ingredientType][ingredient.name]['unit_of_measure'] = ingredient.unit_of_measure

        return Response(dict(ingredient_totals))