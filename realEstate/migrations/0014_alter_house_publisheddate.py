# Generated by Django 5.0.4 on 2024-05-15 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0013_house_mainphoto_alter_house_publisheddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 18, 20, 55, 553593)),
        ),
    ]
