from django import template
from django.shortcuts import render_to_response
from django.template.context_processors import csrf


register = template.Library()

@register.index
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('app_url_shortener/index.html', c)