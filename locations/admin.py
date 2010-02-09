from django.contrib import admin

from locations.models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('minimap', 'hint', 'point_coords')
    list_display_links = ('minimap', 'hint',)

admin.site.register(Location, LocationAdmin)