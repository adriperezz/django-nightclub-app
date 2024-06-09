from datetime import date, timezone
import os
from django.db import models
from django.contrib.postgres.fields import ArrayField
from djangoApp.settings import STATIC_URL

TYPE_BUSINESS = (
    ('rent', 'Alquilar'),
    ('sell', 'Vender'),
    ('transfer', 'Traspasar'),
    ('sold', 'Vendido')
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
        ('casa_rustica', 'Casa rustica'),
        ('villa', 'Villa')
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
    ('ground', 'Baja'),
    ('none', 'None')
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
    new_name = f"{instance.relatedOffice.reference}"
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(filename)
    #Guardamos la variable de la carpeta donde meter el archivo
    url = f"{STATIC_URL}/uploads/realEstate/officesPhotos/{new_name}/"
    
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
    new_name = f"{instance.relatedHouse.reference}"
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(filename)
    #Guardamos la variable de la carpeta donde meter el archivo
    url = f"{STATIC_URL}/uploads/realEstate/housesPhotos/{new_name}/"
    
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

def uploadMainPhoto(instance, filename):
    
    # Obtener el la referencia del inmueble
    new_name = f"{instance.reference}"
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(filename)
    #Guardamos la variable de la carpeta donde meter el archivo
    url = f"{STATIC_URL}/uploads/realEstate/housesPhotos/{new_name}/0_mainPhoto{extension}"

    if os.path.exists(url):
        os.remove(url)

    return url

def agentFileName(instance, filename):
    # Obtener el nombre y apellido del agente
    new_name = f"{instance.fullName}"
    
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(filename)
    url = f"{STATIC_URL}/uploads/realEstate/agentsPhoto/{new_name}{extension}"
    if os.path.exists(url):
        os.remove(url)

    # Devolver la ruta de destino completa
    return url

class OpeningHours(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')
        verbose_name_plural = "Horario"

    def __unicode__(self):
        return f'{self.get_weekday_display()} / {self.from_hour} - {self.to_hour}'
    
    def __str__(self):
        return f'{self.get_weekday_display()} / {self.from_hour} - {self.to_hour}'

class Address(models.Model):
    street = models.CharField(max_length=120)
    number = models.CharField(max_length=20)
    zipCode = models.IntegerField(default=00000)
    localidad = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=40)

    class Meta:
        abstract = True
    
class OfficeAddress(Address):
    class Meta:
        verbose_name_plural = "Direcciones Oficina"
        unique_together = ('street', 'number', 'zipCode', 'localidad', 'province')

    def __str__(self):
        return f'{self.street}, {self.number}, {self.zipCode} ({self.localidad}, {self.province})'

class HouseAddress(Address):   
    class Meta:
        verbose_name_plural = "Direcciones Casa"
        unique_together = ('street', 'number', 'zipCode', 'localidad', 'province')

    def __str__(self):
        return f"{self.street}, {self.number}, {self.zipCode} ({self.localidad}, {self.province})"


class Office(models.Model):
    office = models.CharField(max_length=40)
    reference = models.CharField(max_length=10, null=True, blank=True, unique=True)
    description = models.TextField()
    openingHours = models.ManyToManyField(OpeningHours)
    phone = models.CharField(max_length=9)
    address = models.OneToOneField(OfficeAddress, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Oficinas"

    def __str__(self):
        return f"{self.office}"
    
class ImageOffice(models.Model):
    relatedOffice = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=uploadOfficeFile)

    class Meta:
        verbose_name_plural = "Imagenes Oficina"

    def __str__(self):
        _, newName = os.path.split(self.image.name)
        return f"{self.relatedOffice.office} / {newName}"
    
class ContactInfo(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to=agentFileName, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Informacion Contacto"

    class Meta:
        abstract = True

class Agent(ContactInfo):
    rol = ArrayField(models.CharField(max_length=20))
    oficina = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)
    idiomas = ArrayField(models.CharField(max_length=25), null=True)
    description = models.TextField()
    bestPhrase = models.CharField()
    linkRRSS = ArrayField(models.CharField(max_length=40))

    class Meta:
        verbose_name_plural = "Agentes"

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
    publishedDate = models.DateTimeField(auto_now_add=True)
    construction_year = models.PositiveIntegerField(default=date.today().year)
    address = models.OneToOneField(HouseAddress, on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    mainPhoto = models.ImageField(upload_to=uploadMainPhoto, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Casas"

    def __str__(self):
        return self.name
    
    """def save(self, *args, **kwargs):
        if not self.id:  # Si es una nueva instancia (no tiene ID)
            self.publishedDate = timezone.now()  # Establecer la fecha y hora actual
        super().save(*args, **kwargs)"""
    
class ImageHouse(models.Model):
    relatedHouse = models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=uploadHouseFile)

    class Meta:
        verbose_name_plural = "Imagenes Casas"

    def __str__(self):
        _, newName = os.path.split(self.image.name)
        return f"{self.relatedHouse.reference} / {newName}"

class User(ContactInfo):
    likedHouses = models.ManyToManyField(House, blank=True)

    @property
    def fullName(self):
        return f"{self.name.lower().replace(' ', '')}{self.lastname.lower().replace(' ', '')}"

    class Meta:
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return f"{self.name} {self.lastname}"
    