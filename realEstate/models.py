from datetime import date
from django.db import models
from django.contrib.postgres.fields import ArrayField
from localflavor.es.forms import (ESPostalCodeField, ESProvinceSelect)

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

WEEKDAYS = [
  (1, ("Monday")),
  (2, ("Tuesday")),
  (3, ("Wednesday")),
  (4, ("Thursday")),
  (5, ("Friday")),
  (6, ("Saturday")),
  (7, ("Sunday")),
]

class OpeningHours(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return f'{self.get_weekday_display()} / {self.from_hour} - {self.to_hour}'
    
    def __str__(self):
        return f'{self.get_weekday_display()} / {self.from_hour} - {self.to_hour}'

class Address(models.Model):
    street = models.CharField(max_length=120)
    number = models.CharField(max_length=20)
    zipCode = models.IntegerField(default=12345)
    localidad = models.CharField(max_length=50)
    province = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.street}, {self.number}, {self.zipCode} ({self.localidad})'

class Office(models.Model):
    office = models.CharField(max_length=40)
    description = models.TextField()
    openingHours = models.ManyToManyField(OpeningHours)
    phone = models.CharField(max_length=9)
    #fotos
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.office}"

class Agent(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    rol = ArrayField(models.CharField(max_length=20))
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    oficina = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    idiomas = ArrayField(models.CharField(max_length=25), null=True)
    photo = models.ImageField(upload_to="realEstate/agentsPhoto/", null=True)
    description = models.TextField()
    bestPhrase = models.CharField()
    linkRRSS = ArrayField(models.CharField(max_length=40))

    def __str__(self):
        return f"{self.name} {self.lastname} ({self.rol})"
    
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
    caracteristicas = ArrayField(models.CharField(max_length=20, default=None), default=None)
    floor = models.CharField(max_length=12, choices=FLOOR)
    publishedDate = models.DateField(default= date.today)
    address = models.CharField()
    zipCode = models.IntegerField()
    city = models.CharField()
    country = models.CharField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, default=None)

    url = "realEstate/housesPhotos/" + str(reference.name)
    #photos = ArrayField(models.ImageField(upload_to=url), null=True)

    def __str__(self):
        return self.name