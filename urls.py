import os.path

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_ROOT, 'media')}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('locations.urls')),
)
