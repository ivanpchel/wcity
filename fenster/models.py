from django.db import models
from django.core.validators import int_list_validator

# Create your models here.
class Fenster (models.Model):
    window_width = models.IntegerField()
    window_height = models.IntegerField()
    window_number = models.IntegerField(default=0)
    window_view = models.CharField(default='', max_length=1024)
    window_scheme = models.CharField(
	validators=[int_list_validator],
	default='1,2',
	max_length=1024
    )
    is_buy = models.BooleanField(default=False)
