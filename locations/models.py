from django.utils.translation import ugettext_lazy as _

from django.contrib.gis.db import models

class Location(models.Model):
    point = models.PointField()
    hint = models.TextField()
    objects = models.GeoManager()
    
    def __unicode__(self):
        return "%s (%s,%s)" % (self.hint, self.point.coords[0], self.point.coords[1])
    
    def point_coords(self):
        return "%s,%s" % (self.point.coords[0], self.point.coords[1])
    point_coords.short_description = _("Coordinates")
    
    def minimap(self):
        return '<img src="http://maps.google.com/staticmap?center=%(lat)s,%(lng)s&amp;markers=%(lat)s,%(lng)s,red&amp;zoom=14&amp;size=128x128&amp;maptype=mobile" alt="" />' % {'lat':self.point.coords[0], 'lng':self.point.coords[1]}
    minimap.allow_tags = True
    minimap.short_description = _("Map")