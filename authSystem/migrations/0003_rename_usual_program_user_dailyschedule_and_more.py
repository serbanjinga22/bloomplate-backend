# Generated by Django 5.0.6 on 2024-05-21 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authSystem', '0002_user_is_active_user_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usual_program',
            new_name='dailySchedule',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='budget',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='alergies_to_exclude',
            new_name='excludedFoods',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='food_preferences',
            new_name='foodPreferences',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='general_mood',
            new_name='generalMood',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='kg',
            new_name='kilograms',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='main_objective',
            new_name='mainObjective',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='no_of_people',
            new_name='noPeople',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='alergies',
            new_name='restrictionDiet',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='time_allocated',
            new_name='weeklyBudget',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='time_buying_allocated',
            new_name='weeklyFood',
        ),
    ]
