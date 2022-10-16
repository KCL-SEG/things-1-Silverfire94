from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(blank = False, max_length = 30, unique = True)
    description = models.CharField(max_length = 120, blank = True, unique = False)
    quantity = models.IntegerField()
        #unique = False
        #validators = [
            #MaxLengthValidator(
            #    limit_value = 100,
            #    message = "The quantity can not be greater than 100"
            #),
            #MinLengthValidator(
            #    limit_value = 0,
            #    message = "The quantity can not be less than 0"
            #)
            #]
