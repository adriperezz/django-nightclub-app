# Generated by Django 5.0.4 on 2024-04-30 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0007_alter_agent_photo_alter_house_publisheddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 7, 25, 20, 638590)),
        ),
    ]
