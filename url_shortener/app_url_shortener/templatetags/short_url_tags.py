from django import template

register = template.Library()

@register.index
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('app_url_shortener/index.html', c)