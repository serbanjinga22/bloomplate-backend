# Generated by Django 5.0.6 on 2024-06-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0011_alter_meal_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='weekNumber',
            field=models.IntegerField(default=1),
        ),
    ]