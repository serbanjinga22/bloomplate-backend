# Generated by Django 5.0.6 on 2024-05-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_alter_meal_mealtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='mealType',
            field=models.CharField(choices=[('Dimineata', 'Dimineata'), ('Pranz', 'Pranz'), ('Cina', 'Cina'), ('Gustare', 'Gustare')], default='Gustare', max_length=255),
        ),
    ]
