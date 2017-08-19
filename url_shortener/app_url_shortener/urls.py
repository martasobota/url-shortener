from django.conf.urls import url
from app_url_shortener.views import index, shorten_url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^shorten_url/$', shorten_url, name='shortenurl'),
]
