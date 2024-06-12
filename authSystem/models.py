from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """ 
        Method to create a normal user with the given email, username, and password.
        It checks if the fiedls are empty, and raises a ValueError if they are.
        """
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The username field must be set')
        if not password:
            raise ValueError('The password field must be set')

        # The email address is normalized to lowercase.
        email = self.normalize_email(email)
        # Creates a new user, but is not saved yet.
        user = self.model(email=email, username=username, **extra_fields)
        # Sets the password, by hashing and salting it.
        user.set_password(password)
        
        # Saves and returns the user instance.
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """ 
        Method to create a super user with the given email, username, and password.
        It assigns the is_staff and is_superuser fields to True.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Calls the create_user method defined above, also passing the extra fields.
        return self.create_user(email, username, password, **extra_fields)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    gender_choices = [
        ('Bărbat', 'Bărbat'),
        ('Femeie', 'Femeie')
    ]

    food_choices = [
        ('Omnivor', 'Omnivor'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
        ('Pescaterian', 'Pescaterian'),
    ]

    main_objective_chocies = [
        ("Stare generală de bine", "Stare generală de bine"),
        ("Digestie îmbunătățită", "Digestie îmbunătățită"),
        ("Echilibru hormonal", "Echilibru hormonal"),
        ("Intolerante", "Intolerante")
    ]

    general_mood_choices = [
        ("Anti-Stres", "Anti-Stres"),
        ("Nivel de energie mai ridicat", "Nivel de energie mai ridicat"),
        ("", "")
    ]

    digestion_choices = [
        ("Anti-Balonare", "Anti-Balonare"),
        ("Anti-Constipație", "Anti-Constipație"),
        ("", "")
    ]

    hormonal_choices = [
        ("Îmbunătățire simptome ovare polichistice", "Îmbunătățire simptome ovare polichistice"),
        ("Îmbunătățire simptome endometrioză", "Îmbunătățire simptome endometrioză"),
        ("", "")
    ]

    intolerancies_choices = [
        ("Fără lactoză", "Fără lactoză"),
        ("Fără gluten", "Fără gluten")
    ]

    alergies_choices = [
        (True, "Da"),
        (False, "Nu")
    ]

    usual_program_choices = [
        ("Timp de lucru complet la birou", "Timp de lucru complet la birou"),
        ("Lucrez de acasă", "Lucrez de acasă"),
        ("Program variabil", "Program variabil"),
        ("Lucrez în schimburi", "Lucrez în schimburi")
    ]

    username = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)
    age = models.IntegerField(default=18, blank=False)
    kilograms = models.IntegerField(default=70, blank=False)
    foodPreferences = models.CharField(max_length=40, blank=False, choices=food_choices)
    mainObjective = models.CharField(max_length=40, blank=False, choices=main_objective_chocies)
    generalMood = models.CharField(max_length=40, blank=True, choices=general_mood_choices)
    digestion = models.CharField(max_length=40, blank=True, choices=digestion_choices)
    hormonal = models.CharField(max_length=40, blank=True, choices=hormonal_choices)
    intolerancies = models.CharField(max_length=40, blank=True, choices=intolerancies_choices)
    excludeFoods = models.BooleanField(default=False, blank=False, choices=alergies_choices)
    excludedFoods = models.CharField(max_length=255, blank=True)
    noPeople = models.IntegerField(default=0, blank=False)
    weeklyBudget = models.IntegerField(default=0, blank=False)
    duration = models.IntegerField(default=0, blank=False)
    weeklyFood = models.IntegerField(default=0, blank=False)
    dailySchedule = models.CharField(max_length=40, blank=False, choices=usual_program_choices)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    lactoseFree = models.BooleanField(default=False)
    glutenFree = models.BooleanField(default=False)
    antiStress = models.BooleanField(default=False)
    energyLevelHigher = models.BooleanField(default=False)
    antiBloating = models.BooleanField(default=False)
    antiConstipation = models.BooleanField(default=False)
    improvementPCOS = models.BooleanField(default=False)
    improvementEndometriosis = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
