# Generated by Django 5.0.4 on 2024-04-23 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realEstate', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=120)),
                ('number', models.CharField(max_length=20)),
                ('zipCode', models.IntegerField(default=0)),
                ('localidad', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Direcciones Oficina',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=120)),
                ('number', models.CharField(max_length=20)),
                ('zipCode', models.IntegerField(default=0)),
                ('localidad', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50, null=True)),
                ('nombreDireccion', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Direcciones Usuario',
            },
        ),
        migrations.AlterModelOptions(
            name='agent',
            options={'verbose_name_plural': 'Agentes'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name_plural': 'Casas'},
        ),
        migrations.AlterModelOptions(
            name='imagehouse',
            options={'verbose_name_plural': 'Imagenes Casas'},
        ),
        migrations.AlterModelOptions(
            name='imageoffice',
            options={'verbose_name_plural': 'Imagenes Oficina'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name_plural': 'Oficinas'},
        ),
        migrations.AlterModelOptions(
            name='openinghours',
            options={'ordering': ('weekday', 'from_hour'), 'verbose_name_plural': 'Horario'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='agent',
            name='oficina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='realEstate.office'),
        ),
        migrations.AlterField(
            model_name='house',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='realEstate.agent'),
        ),
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='realEstate.officeaddress'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
