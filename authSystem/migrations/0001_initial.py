# Generated by Django 5.0.6 on 2024-05-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(default='aiazic@gmail.com', max_length=100, unique=True)),
                ('gender', models.CharField(choices=[('BARBAT', 'Barbat'), ('FEMEIE', 'Femeie')], max_length=20)),
                ('age', models.IntegerField(default=18)),
                ('kg', models.IntegerField(default=70)),
                ('food_preferences', models.CharField(choices=[('OMNIVOR', 'Omnivor'), ('VEGETARIAN', 'Vegetarian'), ('VEGAN', 'Vegan'), ('PESCATARIAN', 'Pescatarian')], max_length=40)),
                ('main_objective', models.CharField(choices=[('STAREGENERALADEBINE', 'Stare generala de bine'), ('DIGESTIEIMBUNATATITA', 'Digestie imbutanatita'), ('ECHILIBRUHORMONAL', 'Echilibriu hormonal'), ('INTOLERANTE', 'Intolerante')], max_length=40)),
                ('general_mood', models.CharField(choices=[('ANTI STRES', 'Anti Stres'), ('NIVELDEENERGIEMAIRIDICAT', 'Nivel de energie mai ridicat')], max_length=40)),
                ('digestion', models.CharField(choices=[('ANTIBALONARE', 'Anti-Balonare'), ('ANTICONSTIPATIE', 'Anti-Constipatie')], max_length=40)),
                ('hormonal', models.CharField(choices=[('IMBUNATATIRE1', 'Imbunatatire simptome ovare polichistice'), ('IMBUNATATIRE2', 'Imbunatatire simptome endometrioza')], max_length=40)),
                ('intolerancies', models.CharField(choices=[('FARALACTOZA', 'Fara lactoza'), ('FARAGLUTEN', 'Fara gluten')], max_length=40)),
                ('alergies', models.CharField(choices=[('DA', 'Da'), ('NU', 'Nu')], max_length=40)),
                ('alergies_to_exclude', models.CharField(max_length=255)),
                ('no_of_people', models.IntegerField(default=0)),
                ('budget', models.IntegerField(default=0)),
                ('time_allocated', models.IntegerField(default=0)),
                ('time_buying_allocated', models.IntegerField(default=0)),
                ('usual_program', models.CharField(choices=[('TIMPDELUCRU', 'Timp de lucru complet la birou'), ('LUCREZDEACASA', 'Lucrez de acasa'), ('PROGRAMVARIABIL', 'Program Variabil'), ('LUCREZINSCHIMBURI', 'Lucrez in schimburi')], max_length=40)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
