from datetime import date
from django.db import models
from django.contrib.postgres.fields import ArrayField

TYPE_BUSINESS = (
    ('rent', 'Alquilar'),
    ('sell', 'Vender'),
    ('transfer', 'Traspasar')
)

TYPE_HOUSE = (
    ('Pisos', (
        ('piso', 'Piso'),
        ('atico', 'Atico'),
        ('duplex', 'Duplex'),
    )),
    ('Casas y Chalets', (
        ('independiente', 'Independiente'),
        ('pareado', 'Pareado'),
        ('adosada', 'Adosada'),
        ('casa_rustica', 'Casa rustica')
    )),
    ('Comerciales', (
        ('trastero', 'Trastero'),
        ('local_comercial', 'Local Comercial'),
    ))
)

STATE = (
    ('new', 'Obra nueva'),
    ('good', 'Buen estado'),
    ('bad', 'A reformar')
)

FLOOR = (
    ('last', 'Ultima'),
    ('middle', 'Intermedias'),
    ('ground', 'Baja')
)

class House(models.Model):
    name = models.CharField(max_length=70)
    summary = models.CharField()
    description = models.TextField()
    reference = models.CharField(max_length=10, unique=True)
    typeBusiness = models.CharField(max_length=10, choices=TYPE_BUSINESS)
    typeHouse = models.CharField(max_length=15, choices=TYPE_HOUSE)
    price = models.FloatField()
    metrosUtiles = models.FloatField()
    metrosConstruidos = models.FloatField()
    numBedrooms = models.PositiveIntegerField()
    numBathrooms = models.PositiveIntegerField()
    state = models.CharField(max_length=14, choices=STATE)
    #caracteristicas
    floor = models.CharField(max_length=12, choices=FLOOR)
    publishedDate = models.DateField(default= date.today)
    address = models.CharField()
    zipCode = models.IntegerField()
    city = models.CharField()
    country = models.CharField()
    #photos
    #agent

class Agent(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    rol = ArrayField(models.CharField(max_length=20))
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    #oficina
    #idiomas ver que hacer checkbox
    #photo
    description = models.TextField()
    bestPhrase = models.CharField()
    linkRRSS = ArrayField(models.CharField(max_length=40))
    
    

