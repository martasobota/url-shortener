from django.conf.urls import url, patterns, include
 
urlpatterns = patterns('app_url_shortener.views',
    url(r'^$', 'index', name='home'),
    url(r'^(?P&lt;short_id&gt;\w{6})$', 'redirect_to_original', name='redirectoriginal')
    url(r'^shorten/$', 'shorten_url', name='shortenurl'),
    )