# Generated by Django 5.0.4 on 2024-06-13 18:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0020_remove_agent_bestphrase_remove_agent_linkrrss'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='bestPhrase',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='linkRRSS',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), null=True, size=None),
        ),
    ]
