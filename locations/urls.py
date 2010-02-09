from django.conf.urls.defaults import *

urlpatterns = patterns('locations.views',
    url(r'^$', 'index', name='locations_index'),
    url(r'^add/$', 'add_location', name='locations_add'),
    url(r'^locations/$', 'get_locations', name='locations_get_locations'),
)
