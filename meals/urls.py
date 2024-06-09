from django.urls import path
from .api import MealList, MealDetail, MealMatchUser, IngredientTotals

urlpatterns = [
    path('meals/', MealList.as_view(), name='meal-list'),
    path('meals/<int:pk>/', MealDetail.as_view(), name='meal-detail'),
    path('meals/user-meal-match/<int:user_id>/', MealMatchUser.as_view(), name='user-meal-match'),
    path('meals/shopping-list/<int:user_id>/', IngredientTotals.as_view(), name='shopping-list')
]