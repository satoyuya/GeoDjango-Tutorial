from django.contrib import admin
from world.models import WorldBorder

# Register your models here.
admin.site.register(WorldBorder, admin.GeoModelAdmin)
