from datetime import date
import os
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

def uploadOfficeFile(instance, filename):
    
    # Obtener el la referencia del inmueble
    new_name = f"{instance.reference}"
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(filename)
    #Guardamos la variable de la carpeta donde meter el archivo
    url = f"realEstate/officesPhotos/{new_name}/"
    
    #Si hay files en la carpeta, se ejecuta el bloque entero
    try:
        #Vemos los archvios de la carpeta
        files = os.listdir(url)
        #Creamos un nuevo array
        newFiles = []

        #Nos quedamos con el INT de cada foto y lo add al nuevo array
        for file in files: 
            number, _ = os.path.splitext(file)
            newFiles.append(number)

        #Ordenamos el array
        newFiles.sort()

        #Cogemos el ultimo elemento del array
        lastFile = newFiles[-1]
        contador = int(lastFile)
        contador += 1
        url = f"{url}/{contador}{extension}"

    #En caso de que no haya files en la carpeta, se crea otra
    except:
        contador = 1
        url = f"{url}/{contador}{extension}"

    return url

def uploadHouseFile(instance, filename):
    
    # Obtener el la referencia del inmueble
    new_name = f"{instance.reference}"
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(filename)
    #Guardamos la variable de la carpeta donde meter el archivo
    url = f"realEstate/housesPhotos/{new_name}/"
    
    #Si hay files en la carpeta, se ejecuta el bloque entero
    try:
        #Vemos los archvios de la carpeta
        files = os.listdir(url)
        #Creamos un nuevo array
        newFiles = []

        #Nos quedamos con el INT de cada foto y lo add al nuevo array
        for file in files: 
            number, _ = os.path.splitext(file)
            newFiles.append(number)

        #Ordenamos el array
        newFiles.sort()

        #Cogemos el ultimo elemento del array
        lastFile = newFiles[-1]
        contador = int(lastFile)
        contador += 1
        url = f"{url}/{contador}{extension}"

    #En caso de que no haya files en la carpeta, se crea otra
    except:
        contador = 1
        url = f"{url}/{contador}{extension}"

    return url

def agentFileName(instance, filename):
    # Obtener el nombre y apellido del agente
    new_name = f"{instance.fullName}"
    
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(filename)
    url = f"realEstate/housesPhotos/{new_name}{extension}"
    if os.path.exists(url):
        os.remove(url)

    # Devolver la ruta de destino completa
    return f"realEstate/agentsPhoto/{new_name}{extension}"

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
    reference = models.CharField(max_length=10, null=True, blank=True, unique=True)
    description = models.TextField()
    openingHours = models.ManyToManyField(OpeningHours)
    phone = models.CharField(max_length=9)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.office}"
    
class OfficeImage(models.Model):
    image = models.ImageField(upload_to=uploadOfficeFile)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

class Agent(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    rol = ArrayField(models.CharField(max_length=20))
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    oficina = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    idiomas = ArrayField(models.CharField(max_length=25), null=True)
    photo = models.ImageField(upload_to=agentFileName, null=True)
    description = models.TextField()
    bestPhrase = models.CharField()
    linkRRSS = ArrayField(models.CharField(max_length=40))

    @property
    def fullName(self):
        return f"{self.name.lower().replace(' ', '')}{self.lastname.lower().replace(' ', '')}"

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

    def __str__(self):
        return self.name
    
class HouseImage(models.Model):
    image = models.ImageField(upload_to=uploadHouseFile)
    house = models.ForeignKey(House, on_delete=models.CASCADE)