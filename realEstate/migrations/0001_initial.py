# Generated by Django 5.0.4 on 2024-04-23 09:07

import datetime
import django.contrib.postgres.fields
import django.db.models.deletion
import realEstate.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=120)),
                ('number', models.CharField(max_length=20)),
                ('zipCode', models.IntegerField(default=12345)),
                ('localidad', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('rol', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('idiomas', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), null=True, size=None)),
                ('photo', models.ImageField(null=True, upload_to=realEstate.models.agentFileName)),
                ('description', models.TextField()),
                ('bestPhrase', models.CharField()),
                ('linkRRSS', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('summary', models.CharField()),
                ('description', models.TextField()),
                ('reference', models.CharField(max_length=10, unique=True)),
                ('typeBusiness', models.CharField(choices=[('rent', 'Alquilar'), ('sell', 'Vender'), ('transfer', 'Traspasar')], max_length=10)),
                ('typeHouse', models.CharField(choices=[('Pisos', [('piso', 'Piso'), ('atico', 'Atico'), ('duplex', 'Duplex')]), ('Casas y Chalets', [('independiente', 'Independiente'), ('pareado', 'Pareado'), ('adosada', 'Adosada'), ('casa_rustica', 'Casa rustica')]), ('Comerciales', [('trastero', 'Trastero'), ('local_comercial', 'Local Comercial')])], max_length=15)),
                ('price', models.FloatField()),
                ('metrosUtiles', models.FloatField()),
                ('metrosConstruidos', models.FloatField()),
                ('numBedrooms', models.PositiveIntegerField()),
                ('numBathrooms', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('new', 'Obra nueva'), ('good', 'Buen estado'), ('bad', 'A reformar')], max_length=14)),
                ('caracteristicas', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=20), default=None, size=None)),
                ('floor', models.CharField(choices=[('last', 'Ultima'), ('middle', 'Intermedias'), ('ground', 'Baja')], max_length=12)),
                ('publishedDate', models.DateField(default=datetime.date.today)),
                ('address', models.CharField()),
                ('zipCode', models.IntegerField()),
                ('city', models.CharField()),
                ('country', models.CharField()),
                ('agent', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='realEstate.agent')),
            ],
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=realEstate.models.uploadHouseFile)),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realEstate.house')),
            ],
            options={
                'ordering': ('house', 'image'),
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=40)),
                ('reference', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=9)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='realEstate.address')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='oficina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realEstate.office'),
        ),
        migrations.CreateModel(
            name='OfficeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=realEstate.models.uploadOfficeFile)),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realEstate.office')),
            ],
            options={
                'ordering': ('office', 'image'),
            },
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
            ],
            options={
                'ordering': ('weekday', 'from_hour'),
                'unique_together': {('weekday', 'from_hour', 'to_hour')},
            },
        ),
        migrations.AddField(
            model_name='office',
            name='openingHours',
            field=models.ManyToManyField(to='realEstate.openinghours'),
        ),
    ]
