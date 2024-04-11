from django.contrib import admin
from .models import House, Agent, Office, OpeningHours, Address

admin.site.register(House)
admin.site.register(Agent)
admin.site.register(Office)
admin.site.register(OpeningHours)
admin.site.register(Address)