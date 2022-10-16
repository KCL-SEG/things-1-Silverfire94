from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField( blank = False, max_length = 20)
    description = models.CharField(max_length = 100, blank = False)
    quantity = models.IntegerField()
