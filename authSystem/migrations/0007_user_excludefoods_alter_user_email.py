# Generated by Django 5.0.6 on 2024-05-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authSystem', '0006_remove_user_restrictiondiet'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='excludeFoods',
            field=models.BooleanField(choices=[(True, 'Da'), (False, 'Nu')], default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
