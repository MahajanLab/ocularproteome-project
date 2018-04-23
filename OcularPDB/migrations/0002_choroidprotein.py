# Generated by Django 2.0.1 on 2018-02-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OcularPDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoroidProtein',
            fields=[
                ('ens_id', models.CharField(default='x', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('fovea_avg', models.IntegerField()),
                ('macula_avg', models.IntegerField()),
                ('periphery_avg', models.IntegerField()),
            ],
        ),
    ]
