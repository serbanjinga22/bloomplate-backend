from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'gender', 'age', 'kilograms', 'foodPreferences', 'mainObjective', 'generalMood', 'digestion', 'hormonal', 'intolerancies', 'excludeFoods', 'excludedFoods', 'noPeople', 'weeklyBudget', 'duration', 'weeklyFood', 'dailySchedule', 'lactoseFree', 'glutenFree', 'antiStress', 'energyLevelHigher', 'antiBloating', 'antiConstipation', 'improvementPCOS', 'improvementEndometriosis')

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()