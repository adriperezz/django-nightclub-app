# Generated by Django 5.0.4 on 2024-05-09 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0008_alter_house_publisheddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='prueba',
            field=models.CharField(default='Hola', max_length=10),
        ),
        migrations.AlterField(
            model_name='house',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 9, 16, 31, 21, 973285)),
        ),
    ]