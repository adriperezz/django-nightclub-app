from django.contrib import admin
from .models import *

admin.site.register(House)
admin.site.register(Agent)
admin.site.register(Office)
admin.site.register(OpeningHours)
admin.site.register(OfficeAddress)
admin.site.register(HouseAddress)
admin.site.register(ImageHouse)
admin.site.register(ImageOffice)