from django.contrib import admin
from app_url_shortener.models import URLs

# Register your models here.
 
class URLsAdmin(admin.ModelAdmin):
    list_display = ('short_id','httpurl','date_time', 'count')
    ordering = ('-date_time',)
 
admin.site.register(URLs, URLsAdmin)