
from south.db import db
from django.db import models
from locations.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('locations_location', (
            ('id', orm['locations.Location:id']),
            ('point', orm['locations.Location:point']),
            ('hint', orm['locations.Location:hint']),
        ))
        db.send_create_signal('locations', ['Location'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('locations_location')
        
    
    
    models = {
        'locations.location': {
            'hint': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('models.PointField', [], {})
        }
    }
    
    complete_apps = ['locations']
