from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(blank = False, max_length = 30, unique = True)
    description = models.CharField(max_length = 120, blank = True, unique = False)
    quantity = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)])
