# Generated by Django 2.0.1 on 2018-03-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OcularPDB', '0005_auto_20180307_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retinaprotein',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
