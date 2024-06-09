from rest_framework import generics
from .models import Ingredient
from .serializers import IngredientSerializer

class IngredientRetrievAPIView(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'id'