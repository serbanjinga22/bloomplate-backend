# Generated by Django 5.0.6 on 2024-06-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authSystem', '0012_rename_antibloatinganti_balonare_user_antibloating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='generalMood',
            field=models.CharField(blank=True, choices=[('Anti-Stres', 'Anti-Stres'), ('Nivel de energie mai ridicat', 'Nivel de energie mai ridicat'), ('', '')], max_length=40),
        ),
    ]
