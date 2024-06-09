# Generated by Django 5.0.6 on 2024-05-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_alter_meal_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='mealType',
            field=models.CharField(choices=[('Dimineata', 'Dimineata'), ('Pranz', 'Pranz'), ('Cina', 'Cina')], default='Dimineata', max_length=255),
        ),
    ]
