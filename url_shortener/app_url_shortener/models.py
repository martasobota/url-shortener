from django.db import models

# Create your models here.
class URLs(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True)
    httpurl = models.URLField(max_length=200)
    date_time = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
 
    def __str__(self):
	    return self.httpurl
