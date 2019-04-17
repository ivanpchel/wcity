from django.db import models

# Create your models here.
class Fenster (models.Model):
    window_width = models.IntegerField()
    window_height = models.IntegerField()
    window_number = models.IntegerField(default=0)
    window_view = models.CharField(default='', max_length=1024)
