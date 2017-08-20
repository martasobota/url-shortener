import random, string, json
import logging
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.template.context_processors import csrf

from app_url_shortener.models import URLs


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('app_url_shortener/index.html', c)
 
def redirect_original(request, short_id):
    url = get_object_or_404(URLs, pk=short_id) # get object, if not found return 404 error
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)

def shorten_url(request):
    url = request.POST.get('url', '')
    try:
        get_url = URLs.objects.get(httpurl=url)
        short_id = get_url.short_id
    except URLs.DoesNotExist:
        logging.error('URL does not exist')
    if not (url == ''):
        short_id = getShortCode()
        b = URLs(httpurl=url, short_id=short_id)
        b.save()
        response_data = {}
        response_data['url'] = settings.SITE_URL + '/' + short_id
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'error': 'error occurs'}),content_type='application/json')
    
def create_short_url():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = URLs.objects.get(pk=short_id)
        except:
            return short_id
