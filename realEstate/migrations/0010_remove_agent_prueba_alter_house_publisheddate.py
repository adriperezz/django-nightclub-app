# Generated by Django 5.0.4 on 2024-05-09 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0009_agent_prueba_alter_house_publisheddate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='prueba',
        ),
        migrations.AlterField(
            model_name='house',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 9, 16, 32, 27, 87955)),
        ),
    ]
