# Generated by Django 5.0.4 on 2024-04-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='reference',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]