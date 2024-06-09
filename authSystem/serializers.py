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
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'gender', 'age', 'kilograms', 'foodPreferences', 'mainObjective', 'generalMood', 'digestion', 'hormonal', 'intolerancies', 'excludeFoods', 'excludedFoods', 'noPeople', 'weeklyBudget', 'duration', 'weeklyFood', 'dailySchedule')

        def create(self, validated_data):
            user = User.objects.create(**validated_data)
            return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()