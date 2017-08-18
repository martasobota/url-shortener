from django.conf.urls import url
 
# urlpatterns = patterns('app_url_shortener.views',
#     url(r'^$', 'index', name='home'),
#     url(r'^shorten/$', 'shorten_url', name='shortenurl'),
#     )

urlpatterns = [
	# 'app_url_shortener.views',
    url(r'^$', 'index', name='home'),
    url(r'^shorten/$', 'shorten_url', name='shortenurl'),
]
