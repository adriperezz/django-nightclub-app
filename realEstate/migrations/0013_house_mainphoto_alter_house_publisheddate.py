# Generated by Django 5.0.4 on 2024-05-15 16:20

import datetime
import realEstate.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0012_alter_house_publisheddate_alter_houseaddress_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='mainPhoto',
            field=models.ImageField(blank=True, null=True, upload_to=realEstate.models.uploadMainPhoto),
        ),
        migrations.AlterField(
            model_name='house',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 18, 20, 49, 928569)),
        ),
    ]