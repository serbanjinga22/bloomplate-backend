# Generated by Django 5.0.6 on 2024-05-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit_of_measure',
            field=models.CharField(choices=[('g', 'Grams'), ('kg', 'Kilograms'), ('ml', 'Milliliters'), ('l', 'Liters'), ('tsp', 'Teaspoons'), ('tbsp', 'Tablespoons'), ('cup', 'Cups'), ('piece', 'Pieces')], default='g', max_length=255),
        ),
    ]
