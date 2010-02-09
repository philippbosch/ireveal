from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.utils.encoding import force_unicode

from django.contrib.gis.geos import Point

from locations.models import Location

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def add_location(request):
    if not request.POST.get('point', None):
        return HttpResponseBadRequest()
    point = request.POST['point'].split(',')
    hint = request.POST.get('hint', "")
    l = Location.objects.create(point=Point(float(point[0]),float(point[1])), hint=hint)
    return HttpJsonResponse({'lat': l.point.coords[0], 'lng': l.point.coords[1], 'hint': l.hint})

def get_locations(request):
    locations = Location.objects.all()
    data = []
    for l in locations:
        data.append({'lat': l.point.coords[0], 'lng': l.point.coords[1], 'hint': l.hint})
    return HttpJsonResponse(data)

class HttpJsonResponse(HttpResponse):
    def __init__(self, content, mimetype=None, status=None, content_type=None, fields=None):
        content_type = 'application/json'
        content_type = 'text/plain' # TODO!
        content = simplejson.dumps(content)
        return super(HttpJsonResponse, self).__init__(content=content, status=status, content_type=content_type)
