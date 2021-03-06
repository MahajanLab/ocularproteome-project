# Generated by Django 2.0.1 on 2018-03-28 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OcularPDB', '0008_mouseprotein'),
    ]

    operations = [
        migrations.CreateModel(
            name='MouseRetina',
            fields=[
                ('ens_id', models.CharField(default='x', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MouseVitreous',
            fields=[
                ('ens_id', models.CharField(default='x', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='MouseProtein',
        ),
    ]
