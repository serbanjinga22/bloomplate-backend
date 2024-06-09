from django.urls import path
from .api import IngredientRetrievAPIView

urlpatterns = [
    path('ingredient/<int:id>/', IngredientRetrievAPIView.as_view(), name='ingredient-detail'),
]